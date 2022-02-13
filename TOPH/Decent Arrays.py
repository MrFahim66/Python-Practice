N = int(input())
count = 0

lst = list(map(int, input().split()))

lst2 = sorted(lst)

if lst == lst2:
    print("Yes")
else:
    print("No")