n = int(input())

for i in range(0, n):
    problem = int(input())
    if( problem > 10):
        print('10', problem-10)
    else:
        print('0', problem)
