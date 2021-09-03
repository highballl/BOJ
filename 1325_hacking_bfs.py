import sys
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

result = []
max_count = -1

for i in range(1, n+1):
    visited = [False]*(n+1)
    q = deque([i])
    visited[i] = True
    count = 1
    while q:
        curr = q.popleft()
        for num in graph[curr]: 
            if visited[num] == False:
                q.append(num)
                visited[num] = True
                count += 1
    if count > max_count:
        max_count = count
        result = []
        result.append(i)
    elif max_count == count:
        result.append(i)

for i in range(len(result)):
    print(result[i], end=" ")
