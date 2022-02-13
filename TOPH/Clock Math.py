H,M = input().split()

H = int(H)
M = int(M)

Hours = (H*60+M) *0.5
Minutes = M*6

result = abs(0.5*(60*H - 11*M))

if(result > 180):
    result = 360 - result

formatted_result = "{:.7f}".format(result)

print(formatted_result)