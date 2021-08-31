n = int(input())
nums = list([input().strip() for _ in range(n)])

def sum_num(num):
    sum_num = 0
    #check = ""
    for i in range(len(num)):
        if num[i].isdigit():
            sum_num += int(num[i])
            #check += num[i].strip()
    return sum_num

result = sorted(nums, key = lambda x: (len(x), sum_num(x), x))


print('\n'.join(result))


# check을 쓸데없이 넣어서 틀렸었다.

# n = int(input())
# nums = list([input().strip() for _ in range(n)])

# def sum_num(num):
#     sum_num = 0
#     check = ""
#     for i in range(len(num)):
#         if num[i].isdigit():
#             #print("num[i]",num[i])
#             sum_num += int(num[i])
#             check += num[i].strip()
#     return sum_num, check
#     #sums[nums.index(num)] = sum_num

# #print(sum_num(nums[1]))

# # def check_digit(num):
# #     check = ""
# #     for i in range(len(num)):
# #         if num[i].isdigit():
# #             check += num[i].strip()
# #     return int(check)
# #result = sorted(nums, key = lambda x: (len(x), sum_num(x), check_digit(x)))
# result = sorted(nums, key = lambda x: (len(x), sum_num(x)))


# print('\n'.join(result))


# # 중요반례
# # 2
# # AA12
# # AA03 

# # 중요반례
# # 2
# # AA1
# # A1A
# answer:
# # A1A
# # AA1