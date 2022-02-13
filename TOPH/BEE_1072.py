n = int(input())

count1 = 0
coutn2 = 0

for i in range(0, n):
    x = int(input())
    if x >= 10 and x <= 20:
        count1+=1
    else:
        coutn2+=1

print(count1,"in")
print(coutn2,"out")