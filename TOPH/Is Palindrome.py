String1 = input()

myString = String1.casefold()

revString = reversed(String1)

if list(myString) == list(revString):
    print('Yes')
else:
    print('NO')