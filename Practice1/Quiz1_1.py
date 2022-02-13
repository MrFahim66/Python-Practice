List = [-2,5,6,2,-15,-79,3245,12,-123,423]

positive = 0
negative = 0

for i in range(0, len(List)):
    if(List[i]>= 0):
        positive+=1
    elif(List[i]<=0):
        negative+=1

print(positive,negative)