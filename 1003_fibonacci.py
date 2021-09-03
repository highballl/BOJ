import sys
from collections import defaultdict
T = int(input())
nums = list([int(sys.stdin.readline().strip()) for _ in range(T)])

memo_0 = defaultdict(int)
memo_1 = defaultdict(int)
memo_0 = {0:1, 1:0, 2:1}
memo_1 = {0:0, 1:1, 2:1}

def count_zero(n):
    global count_0
    if n == 0:
        return 1
    elif n == 1:
        return 0
    if n in memo_0:
        return memo_0[n]
    else:
        memo_0[n] = count_zero(n-1) + count_zero(n-2)
        return memo_0[n]


def count_one(n):
    global count_1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n in memo_1:
        return memo_1[n]
    else:
        memo_1[n] = count_one(n-1) + count_one(n-2)
        return memo_1[n]



for n in nums:
    count_0 = 0
    count_1 = 0
    print(count_zero(n), count_one(n))
    


memo = defaultdict(int)
memo = {
    0: 0,
    1: 1,
    2: 1
}

def fibo(n):
    global count_0
    global count_1
    if n == 0:
        print(0)
        count_0 += 1
        memo_0[n] = count_0
        print("count_0", count_0)
        return 0
    elif n == 1:
        print(1)
        count_1 += 1
        print("count_1", count_1)
        memo_1[n] = count_1
        return 1
    if n in memo:
        print(n)
        memo_1[n] = count_1
        memo_0[n] = count_0
        return memo[n]
    else:
        print(n)
        memo[n] = fibo(n-1) + fibo(n-2)
        memo_0[n] = memo_0[n-1] + memo_0[n-2]
        memo_1[n] = memo_1[n-1] + memo_1[n-2]
        return memo[n]
        #return fibo(n-1) + fibo(n-2)


