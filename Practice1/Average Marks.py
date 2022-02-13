#Python Program to Print Roll and Average Marks of 8 Students
for i in range(1, 9):
    print("\nEnter Student", i, "Roll :")
    Student_Roll = int(input())
    print("Enter Mark for Subject 1 : ")
    Mark1 = int(input())
    print("Enter Mark for Subject 2 : ")
    Mark2 = int(input())
    print("Enter Mark for Subject 3 : ")
    Mark3 = int(input())
    Average_Mark = (Mark1 + Mark2 + Mark3) / 3
    if (Average_Mark <= 100):
        print("    Student of Roll", Student_Roll, "Got", Average_Mark, "Marks")
    else:
        print("Error! Please Enter Marks Correctly!")
