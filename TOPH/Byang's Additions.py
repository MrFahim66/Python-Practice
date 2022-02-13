num1, num2 = list(map(int, input().split()))
count = 0
store = 0

while num1 != 0 and num2 != 0:
    store = num1 % 10 + num2 % 10
    num1 /= 10
    num2 /= 10

    if store > 9:
        count += 1
        break

if (count == 0):
    print("No")
else:
    print("Yes")
