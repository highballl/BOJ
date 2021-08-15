# 잃어버린 괄호
import sys
oper = sys.stdin.readline().strip().split("-")
result = []
answer = 0

for i in oper:
    result.append(list(map(int, i.split("+"))))
#print(result)
#print(sum(result[1]))
for i in range(len(result)):
    if i == 0:
        answer += sum(result[i])
    else:
        answer -= sum(result[i])

print(answer) 
