import sys

n = int(input())
nums = [sys.stdin.readline().strip() for _ in range(n)]
#print(nums)

length = len(nums[0])
count = length - 1

    
while count > -1:
    new_arr = []
    for num in nums:
        new_arr.append(num[count:])
    if len(new_arr) != len(set(new_arr)):
        count -= 1
    elif len(new_arr) == len(set(new_arr)) and count != length:
        print(length-count)
        break
    elif len(new_arr) == len(set(new_arr)) and count == length:
        print(length)
        break

#print(new_arr)