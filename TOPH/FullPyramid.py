n = int(input())

for i in range(0, n):
    for j in range(i, n-1):
        print(" ", end ='')

    for j in range(0, i+1):
        if j == i:
            print("*", end ='')
        else:
            print("* ", end='')
    print()