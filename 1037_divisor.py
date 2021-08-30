import sys

n = int(input())
divisors = list(map(int, sys.stdin.readline().split()))

minimum = min(divisors)
maximum = max(divisors)
print(minimum*maximum)