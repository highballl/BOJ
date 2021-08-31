from collections import defaultdict

n = int(input())
memo = defaultdict(int)

def division(n):
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1
    for i in range(4, n+1):
        if i not in memo:
            if i % 3 == 0 and i % 2 !=0:
                memo[i] = min(memo[i//3], memo[i-1]) + 1
            elif i % 3 == 0 and i % 2 == 0:
                memo[i] = min(memo[i//3], memo[i//2], memo[i-1]) + 1
            elif i % 3 != 0 and i % 2 == 0:
                memo[i] = min(memo[i//2], memo[i-1]) + 1
            else:
                memo[i] = memo[i-1]+1
    return memo[n]

print(division(n))

# top-down, recursive error
# def division(n):
#     if n == 1:
#         memo[1] = 0
#     if n == 2:
#         memo[2] = 1
#     if n == 3:
#         memo[3] = 1
#     if n > 3 and n not in memo:
#         if n % 3 == 0 and n % 2 !=0:
#              memo[n] = min(division(n//3), division(n-1))+1
#         elif n % 3 == 0 and n % 2 == 0:
#             memo[n] = min(division(n//3), division(n//2), division(n-1))+1
#         elif n % 3 != 0 and n % 2 != 0:
#             memo[n] = min(division(n//2), division(n-1))+1
#         else:
#             memo[n] = division(n-1)+1
    
#     return memo[n]
