"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __eq__(self, student):
        return self.name == student.name

    def __ge__(self, student):
        return self.name == student.name or self.name>student.name

    def __lt__(self, student):
        return self.name<student.name
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    student = Student("Ken", 5)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)

    student2 = Student("Cliff", 5)
    for i in range(1, 6):
        student2.setScore(i, 30)
    print(student2)

    """Equality Test."""
    print("\nChecking Equality Test for Student 1 and 2")
    print(student.__eq__(student2))

    """Greater Than Test."""
    print("\nChecking Greater Than Test or Equal for Student 1 and 2")
    print(student.__ge__(student2))

    """Less Than Test"""
    print("\nChecking Less Than Test for Student 1 and 2")
    print(student.__lt__(student2))

if __name__ == "__main__":
    main()


