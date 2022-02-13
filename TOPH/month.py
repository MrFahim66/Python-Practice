pos = 0
neg = 0
even = 0
odd = 0

for i in range(0, 5):
    n = float(input())
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1

    if n % 2 == 0:
        even += 1
    elif n % 2 != 0:
        odd += 1

print(even, "valor(es) par(es)")
print(odd, "valor(es) impar(es)")
print(pos, "valor(es) positivo(s)")
print(neg, "valor(es) negativo(s)")
