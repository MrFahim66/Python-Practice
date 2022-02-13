x = int(input())
y = int(input())

res = 0

if y < 0:
    for i in range(x, y, -1):
        if i % 2 != 0:
            res += i
else:
    for i in range(y, x):
        if i % 2 != 0:
            res += abs(i)

print(res)
