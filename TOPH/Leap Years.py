Year = int(input())

if(Year % 4 ==0):
    if(Year % 400 == 0):
        print('No')
    else:
        print('Yes')
else:
    print('No')