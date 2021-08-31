import sys
from collections import deque


def dfs(start):
    visited = {}
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited and graph.get(n) == None:
            visited[n] = 1
            print(n, end="")
        elif n not in visited and graph.get(n) != None:
            visited[n] = 1
            print(n, end=" ")
            # reverse_keys = sorted(graph.keys(), reverse=True)
            # if n not in reverse_keys:
            #     for key in reverse_keys:
            #         if key not in visited and len(graph[key]) > 0:
            #             stack.append(key)
            #             # temp = sorted(graph[key])
            #             # for num in temp:
            #             #     if num not in visited:
            #             #         stack.append(num)
            temp = sorted(graph[n], reverse=True)
            for num in temp:
                if num not in visited:
                    stack.append(num)


    return visited


def bfs(start):
    visited = {}
    q = deque([start])
    while q:
        v = q.popleft()
        if v not in visited and graph.get(v) == None:
            visited[v] = 1
            print(v, end="")
        elif v not in visited and graph.get(v) != None:
            visited[v]=1
            print(v, end=" ")
            # keys = sorted(graph.keys())
            # if v not in keys:
            #     for key in keys:
            #         if key not in visited:
            #             q.append(key)

            temp = sorted(graph[v])
            for num in temp:
                if num not in visited:
                    q.append(num)


    return visited

n, m, start = map(int, sys.stdin.readline().split())
graph = {}
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        pass
    if a in graph:
        graph[a].add(b)
    else:
        graph[a] = {b}
    if b in graph:
        graph[b].add(a)
    else:
        graph[b] = {a}

#print(graph)
dfs(start)
print()
bfs(start)


# print(graph)
#graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
