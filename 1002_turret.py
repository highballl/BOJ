import sys
import math

T = int(input())
cases = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

for x1, y1, r1, x2, y2, r2 in cases:
    d_square = pow(abs(x1-x2), 2) + pow(abs(y1-y2), 2)
    d = math.sqrt(d_square)

    # 서로 다른 두 점에서 원이 만날 때
    if abs(r1-r2) < d < r1+r2:
        print(2)
    # 외접 혹은 내접
    elif d == r1+r2 or d == abs(r1-r2) and d != 0:
        print(1)
    # 만나지 않는 경우
    elif d > r1+r2 or d < abs(r1-r2):
        print(0)
    # 완전히 같은 원
    elif d == 0 and r1 == r2:
        print(-1)
