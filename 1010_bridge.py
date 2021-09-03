import operator
from functools import reduce
import sys

T = int(input())
cases = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
#print(cases[0][0])
def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(operator.mul, range(n, n-r, -1), 1)
    denominator = reduce(operator.mul, range(r, 1, -1), 1)

    return numerator // denominator

for i in range(T):
    print(nCr(cases[i][1], cases[i][0]))