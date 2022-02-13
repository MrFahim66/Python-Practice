n = int(input("Number of Admitted Student:"))
List1 = []
List2 = []

std_id1 = int(input("Enter Student ID: "))
List1.append(std_id1)
for j in range(1, 8):
    print("Subject", j, "Marks:")
    element = int(input())
    List1.append(element)

std_id2 = int(input("Enter Student ID: "))
List2.append(std_id2)
for k in range(1, 8):
    print("Subject", k, "Marks:")
    element = int(input())
    List2.append(element)

List3 = [List1, List2]

List4 = []
List4.append(List1[2])
List4.append(List1[3])
List4.append(List1[6])
List5 = []
List5.append(List2[2])
List5.append(List2[3])
List5.append(List2[6])

List6 = [List4, List5]

print("\nStudents all subject's Marks: ")
for i in range(0, 2):
    for j in range(1, 8):
        print(List3[i][j], end=" ")
    print()

print("\n2D List of 3 subject Marks: ")
for i in range(0, 2):
    for j in range(0, 3):
        print(List6[i][j], end=" ")
    print()

avgMark = (sum(List1)-std_id1) / 7
print("\nAverage Mark of Student 1:", avgMark)