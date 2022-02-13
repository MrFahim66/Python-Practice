sentence1 = input()

list2 = []

list1 = sentence1.split('.')

for ele in list1:
    newList = ele.split()
    list2.append(newList[len(newList)//2])

outputList = []

for x in list2:
    outputList.append(newList[len(newList)-1])

outputSet = set(outputList)

finalOutput = list(outputSet)

print(finalOutput)


