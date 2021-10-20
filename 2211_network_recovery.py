import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = int(1e9)
 
# N, M = map(int, input().split()) # computer 수 N, 회선 정보 M개

# graph = [[] for i in range(N+1)] # M개의 노드만큼 그래프 배열 만들어두기

# for _ in range(M):
#     s, e, c = map(int, input().split()) # start, end, cost
#     graph[s].append((e, c))
#     graph[e].append((s, c))


def dijkstra(start):

    #초기화
    # costs = [INF] * (N+1) # M개의 노드만큼 비용 정보를 담을 배열 초기화(INF)
    # result = [[]] * (N+1)
    # parent = defaultdict()

    q = [] # heapq 를 위해 배열 준비
    heapq.heappush(q, (start, 0)) # 시작 노드, 비용 (비용=0, 자기자신일 때)
    costs[start] = 0 # 시작 노드에서의 비용 0을 따로 저장

    # 탐색
   
    while q : # 큐가 존재한다면, 즉 비어있지 않다면
        now, cost = heapq.heappop(q) # q의 가장 작은 값, 즉 비용이 가장 덜 드는 노드부터 탐색할 것이다 (비용, 현재 노드 순)
        
        if costs[now] < cost: 
            continue
        for i in graph[now]: 
            temp_cost = cost + i[1] 

            if costs[i[0]] > temp_cost : # i[0]은 노드를 의미하는 값, 그 노드에 방문했던 적이 있다면 costs[i][0]값이 존재할 것이고, 새로 계산한 cost와 비교해보자.
                costs[i[0]] = temp_cost # 업데이트 하자
                parent[i[0]] = now
                heapq.heappush(q, (i[0], temp_cost)) # q배열에 (노드 번호, 새 비용)를 푸시한다.

    return costs, parent
                
# 다익스트라 수행

# costs, parent = dijkstra(1)
# print(costs)
# for key in parent.keys():
#     print(key, parent[key])

n, m = map(int, input().split())

costs = [INF] * (n + 1)
parent = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)

print(n - 1)
for i in range(2, n + 1):
    print(i, parent[i])
