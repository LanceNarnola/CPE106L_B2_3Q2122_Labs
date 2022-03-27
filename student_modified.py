import random
class Students(object):

    def __init__(info, name, number):
        info.name = name
        info.grade = []
        for count in range(number):
            info.grade.append(0)

    def getName(info):
        return info.name
    def setScore(info, i, score):
        info.grade[i - 1] = score
    def getScore(info, i):
        return info.grade[i - 1]
    def getAverage(info):
        return sum(info.grade) / len(info._grade)
    def getHighScore(info):
        return max(info.grade)
    def __eq__(info,student):
        return info.name==student.name
    def __lt__(info,student):
        return info.name<student.name
    def __ge__(info,student):
        return info.name>=student.name
    def __str__(info):
        return "Name: " + info.name  + "\nGrade: " + \
               " ".join(map(str, info.grade))

def main():
   
    list=[]
    for count in reversed(range(5)):
        s=Students("Name"+str(count+1),10)
        list.append(s)

    print("Sorted list of the students: ")
    random.shuffle(list)
    list.sort()

    for obj in list:
        print(obj.__str__())


if _name_ == "_main_":
    main()
