from itertools import combinations

n, m, k = map(int, input().split())

# def n_c_m(arr, m):
#     for i in range(len(arr)):
#         if m == 1:
#             yield [arr[i]]
#         else:
#             for next in n_c_m(arr[i+1:], m-1):
#                 yield [arr[i]] + next




def main():
    arr = [i for i in range(n+m)]
    # result = list(n_c_m(arr, m))
    result = list(combinations(arr, m))

    if k > len(result):
        return -1
    else:
        idx = len(result) - k
        elem = result[idx]
        result = ''
        for i in range(n+m):
            if i in elem:
                result += 'z'
            else:
                result += 'a'
        return result
    

print(main())
