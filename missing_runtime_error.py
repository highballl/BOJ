# 잃어버린 괄호
# 런타임 에러
import sys
oper = sys.stdin.readline().strip().split("-")
result = ""
for i in range(len(oper)):
    if i == len(oper)-1:
        result = result + "(" + oper[i] + ")"
    else:
        result = result + "(" + oper[i] + " )" + "-"
print(eval(result)) 
