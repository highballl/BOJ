import math

n = int(input())
num = str(math.factorial(n))
i = len(num)-1
count = 0

if n == 0 or n < 5:
    print(0)
else:
    while i > 0:
        if num[i] != '0':
            print(count)
            break
        elif num[i] == '0':
            i -= 1
            count += 1
            #print("i",i,"count",count,'num[i]',num[i])