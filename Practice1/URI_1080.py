max = -1
position = 0
for i in range(1, 101):
    entry = int(input())
    if entry > max:
        max = entry
        position = i

print(max)
print(position)
