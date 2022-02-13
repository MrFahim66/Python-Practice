t = int(input())
for i in range (0, t):
    n,k = input().split()
    n = int(n)
    k = int(k)

    arr1 = [n][n]

    if n == k:
        if n == 1 or k == 1:
            print("R")
        else:
            print("-1")
    #elif