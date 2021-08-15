# 잃어버린 괄호 _ 또 런타임 에러
import sys
oper = sys.stdin.readline().strip().split("-")
answer = 0

for i in oper:
    if i == oper[0]:
        answer += int(i)
    else:
        answer += -(eval(i))

print(answer)


# result = ""
# for i in oper:
#     if i == oper[-1]:
#         result = result + "(" + i + ")"
#     else:
#         result = result + "(" + i + " )" + "-"
# print(eval(result)) 
