import sys
n = int(input())
words = [sys.stdin.readline().strip() for _ in range(n)]
words = set(words)
result = sorted(words, key= lambda x: (len(x), x))

print('\n'.join(result))