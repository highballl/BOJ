import sys
operation = sys.stdin.readline()

plus = "+"
minus = "-"
result = []

for i in range(len(operation)):
    if operation[i] is minus:
        result.append([minus, i])
    elif operation[i] is plus:
        result.append([plus, i])

print(result)
new_operation = operation
open = []
end = []
loc = 0
count = 0

# for i in range(len(result)-1):
#     if plus in result[i][0]:
#         open.append(result[0][1])
#     if result[i][0] is minus and result[i+1][0] is plus:
#         if i == len(result)-1:
#             open.append(result[i][1]+1)
#         for j in range(i, len(result)-1):
#             if result[j][0] is plus and result[j+1] is minus:
#                 end.append(result[j+1][1])
#             elif minus not in result[j:]:
#                 end.append(result[j][1])
#                 break

for i in range(len(result)-1):
    # if plus not in result[i]:
    #     break
    # elif minus not in result[i]:
    #     break
    if result[i][0] is minus and result[i+1][0] is plus:
        open.append(result[i][1]+1)
    elif result[i][0] is plus and result[i+1][0] is minus:
        end.append(result[i][1])
    elif i+1 == len(result) and result[i+1][0] is plus:
        end.append(-1)

for i in open:
    new_operation = new_operation[:i+count] + "(" + new_operation[i+count:]
    count += 1 

for j in end:
    if j == -1:
        new_operation = new_operation + ")"
    else:
        new_operation = new_operation[:j+count] + ")" + new_operation[j+count:]
        count += 1

print(open)
print(end)
print(new_operation)

# for i in range(len(result)-1):
#     if result[i][0] is minus and result[i+1][0] is plus:
#         for j in range(i, len(result)-1):
#             if result[j][0] is plus and result[j+1][0] is minus:
#                 plus_array.append(result[j][1])
#                 break
#             elif i == len(result)-1:
#                 plus_array.append(result[i][1])
        
#         loc = plus_array[-1]
#         if loc != 0:
#             new_operation = new_operation[:result[i][1]+count] + "(" + new_operation[result[i][1]+count:]
#             count += 1
#             new_operation = new_operation[:result[i][1]+loc+count] + ")" + new_operation[result[i][1]+loc+count:]
#             count += 1
# print(plus_array)
# print(new_operation)



# for i in range(len(result)):
#     loc = 0
#     if i == 0:
#         new_string = operation[:result[i][1]+1] + "(" + operation[result[i][1]+1:]
#         loc += 1
#     elif i % 2 == 1:
#          new_string = new_string[:result[i][1]+loc+1] + ")" + new_string[result[i][1]+loc+1:]
#          loc += 1
#     elif i == result[-1] and len(result) % 2 == 0:
#         pass

# print(new_string)