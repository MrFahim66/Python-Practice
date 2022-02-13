lst = input()
target = int(input())
index2 = 0

for i in range(0, len(lst)):
    for j in range(i, len(lst)):
        if lst[i] + lst[j] == target:
            index2 = j
