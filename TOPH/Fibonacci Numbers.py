Data = int(input())

Num1, Num2 = 0,1

Fibonacci = 1

for i in range(1, Data):
    Fibonacci = Num1 + Num2
    Num1 = Num2
    Num2 = Fibonacci

print(Fibonacci)