import random
import time

"""
    -------DIAMONDS & SEEKERS-------
    Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
    How it will work:
    1. A 8x8 grid will have 8 diamonds of variable length randomly placed about
    2. You will have 50 bullets to take down the ships that are placed down
    3. You can choose a row and column such as A3 to indicate where to shoot
    4. For every shot that hits or misses it will show up in the grid
    5. A diamond cannot be placed diagonally, so if a shot hits the rest of
        the ship is in one of 4 directions, left, right, up, and down
    6. If all ships are unearthed before using up all bullets, you win
        else, you lose
    Legend:
    1. "." = water or empty space
    2. "O" = part of diamond
    3. "X" = part of diamond that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no diamond
"""

# Global variable for grid
grid = [[]]
# Global variable for grid size
grid_size = 8
# Global variable for number of diamonds to place
num_of_diamonds = 2
# Global variable for bullets left
bullets_left = 50
# Global variable for game over
game_over = False
# Global variable for number of ships sunk
num_of_diamonds_sunk = 0
# Global variable for diamonds positions
diamond_positions = [[]]
# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_grid_and_place_diamond(start_row, end_row, start_col, end_col):
    """Will check the row or column to see if it is safe to place a diamond there"""
    global grid
    global diamond_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        diamond_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid


def try_to_place_diamond_on_grid(row, col, direction, length):
    """Based on direction will call helper method to try and place a diamond on the grid"""
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_diamond(start_row, end_row, start_col, end_col)


def create_grid():
    """Will create a 8x8 grid and randomly place down diamonds
       of different sizes in different directions"""
    global grid
    global grid_size
    global num_of_diamonds
    global diamond_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_diamonds_placed = 0

    diamond_positions = []

    while num_of_diamonds_placed != num_of_diamonds:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        diamond_size = random.randint(3, 5)
        if try_to_place_diamond_on_grid(random_row, random_col, direction, diamond_size):
            num_of_diamonds_placed += 1


def print_grid():
    """Will print the grid with rows A-H and columns 0-7"""
    global grid
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def accept_valid_bullet_placement():
    """Will get valid row and column to place bullet shot"""
    global alphabet
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-H) and column (0-7) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-H) for row and (0-7) for column")
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter letter (A-H) for row and (0-7) for column")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter letter (A-H) for row and (0-7) for column")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_placement = True

    return row, col


def check_for_diamond_sunk(row, col):
    """If all parts of a diamond have been shot it is sunk and we later increment diamonds sunk"""
    global diamond_positions
    global grid

    for position in diamond_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Diamond found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True


def shoot_bullet():
    """Updates grid and diamonds based on where the bullet was shot"""
    global grid
    global num_of_diamonds_sunk
    global bullets_left

    row, col = accept_valid_bullet_placement()
    print("")
    print("----------------------------")

    if grid[row][col] == ".":
        print("You missed, no diamond was shot")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_for_diamond_sunk(row, col):
            print("A diamond was completely sunk!")
            num_of_diamonds_sunk += 1
        else:
            print("A diamond was shot")

    bullets_left -= 1


def check_for_game_over():
    """If all diamonds have been sunk or we run out of bullets its game over"""
    global num_of_diamonds_sunk
    global num_of_diamonds
    global bullets_left
    global game_over

    if num_of_diamonds == num_of_diamonds_sunk:
        print("Congrats you won!")
        game_over = True
    elif bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        game_over = True


def main():
    """Main entry point of application that runs the game loop"""
    global game_over

    print("-----Welcome to Battleships-----")
    print("You have 50 bullets to take down 8 diamonds, may the battle begin!")

    create_grid()

    while game_over is False:
        print_grid()
        print("Number of diamonds remaining: " + str(num_of_diamonds - num_of_diamonds_sunk))
        print("Number of bullets left: " + str(bullets_left))
        shoot_bullet()
        print("----------------------------")
        print("")
        check_for_game_over()


if __name__ == '__main__':
    """Will only be called when program is run from terminal or an IDE like PyCharms"""
    main()