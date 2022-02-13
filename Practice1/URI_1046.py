start, end = list(map(int,input().split()))

if(start < end):
    time_diff = end - start
else:
    time_diff = end+24 - start

print("O JOGO DUROU {} HORA(S)".format(time_diff))