entry2 = str(input())

entry2 = entry2.lower()
entry = entry2.capitalize()

for i in range(0, len(entry)):
    if entry[i] == 's':
        print("$", end="")
    elif entry[i] == 'i':
        print("!",end="")
    elif entry[i] == 'o':
        print("()",end="")
    else:
        print(entry[i], end="")
print(".")