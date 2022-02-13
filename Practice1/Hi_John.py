row1 = int(input())
column1 = int(input())
row2 = int(input())
column2 = int(input())

if column1 == column2 or row1 == row2 or abs(column1 - column2) == abs(row1 - row2):
    print("YES")
else:
    print("NO")
