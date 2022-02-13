StudentDictionary = {}


def CGPA_Calculate(courseNumber):
    CGPA = 0
    if (courseNumber >= 80):
        CGPA = 4.00
    elif (courseNumber >= 70):
        CGPA = 3.50
    elif (courseNumber >= 60):
        CGPA = 3.00
    return CGPA


def Average_Number():
    sub1 = int(input("Enter Marks of Subject 1: "))
    sub2 = int(input("Enter Marks of Subject 2: "))
    sub3 = int(input("Enter Marks of Subject 3: "))
    average_Number = (sub1 + sub2 + sub3) / 3
    return average_Number


for i in range(1, 11):
    ID = input("Enter the ID of student:\n")
    if ID == "Q":
        break
    else:
        Name = input("Enter the Name of Student : ")
        CourseName = input("Enter Course Name : ")
        SubjectCode = input("Enter the Subject Code : ")
        AVG_Number = Average_Number()
        StudentCGPA = CGPA_Calculate(AVG_Number)
        StudentDictionary[ID] = [Name, CourseName, SubjectCode, StudentCGPA]

print("Displaying Student Details with CGPA using Dictionary: ")
for key, value in StudentDictionary.items():
    print('Details of ID:', key, ' : ', value)
