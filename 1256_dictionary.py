n, m, k = map(int, input().split())

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

def get_dp(n, m):
    if n==0 or m==0:
        return 1
    if dp[n][m] != 0:
        return dp[n][m]

    dp[n][m] = get_dp(n-1, m) + get_dp(n, m-1)
    return dp[n][m]

def get_result(n, m, k):
    result = ""
    if n == 0:
        result += 'z' * m
        return result
    if m == 0:
        result += 'a'*n
        return result
    if get_dp(n-1, m) > k:
        result += 'a'
        result += get_result(n-1, m, k)
        return result
    else:
        result += 'z'
        result += get_result(n, m-1, k - get_dp(n-1, m))
        return result

def main():
    if k > get_dp(n, m):
        return -1
    else:
        return get_result(n, m, k-1)

print(main())
# def n_c_m(arr, m):
#     for i in range(len(arr)):
#         if m == 1:
#             yield [arr[i]]
#         else:
#             for next in n_c_m(arr[i+1:], m-1):
#                 yield [arr[i]] + next




# def main():
#     arr = [i for i in range(n+m)]
#     # result = list(n_c_m(arr, m))
#     result = list(combinations(arr, m))

#     if k > len(result):
#         return -1
#     else:
#         idx = len(result) - k
#         elem = result[idx]
#         result = ''
#         for i in range(n+m):
#             if i in elem:
#                 result += 'z'
#             else:
#                 result += 'a'
#         return result
    

# print(main())
