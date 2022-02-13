N = int(input())

for i in range(2, N+1):
    if(i == N):
        print('Yes')
    elif(N % i ==0):
        print('No')
        break
