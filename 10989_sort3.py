import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
sort_dict = defaultdict(int)

for _ in range(n):
    num = int(input())
    sort_dict[num] += 1


for key, val in sorted(sort_dict.items()):
    for _ in range(val):
        print(key)
