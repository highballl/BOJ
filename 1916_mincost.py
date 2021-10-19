import heapq, sys
input = sys.stdin.readline
INF = int(1e11)
 
N = int(input()) # 도시의 수 N, 버스의 수 M
M = int(input())

graph = [[] for i in range(N+1)] # M개의 노드(버스의 수)만큼 그래프 배열 만들어두기
costs = [INF] * (N+1) # M개의 노드만큼 비용 정보를 담을 배열 초기화(INF)

for _ in range(M):
    s, e, c = map(int, input().split()) # start, end, cost
    graph[s].append((e, c))

start, end = map(int, input().split()) # 시작점, 도착점
# print(graph)

def dijkstra(start):

    #초기화
    q = [] # heapq 를 위해 배열 준비
    heapq.heappush(q, (start, 0)) # 시작 노드, 비용 (비용=0, 자기자신일 때)
    costs[start] = 0 # 시작 노드에서의 비용 0을 따로 저장


    # 탐색
    while q : # 큐가 존재한다면, 즉 비어있지 않다면
        now, cost = heapq.heappop(q) # q의 가장 작은 값, 즉 비용이 가장 덜 드는 노드부터 탐색할 것이다 (비용, 현재 노드 순)
        if costs[now] < cost: # 최소 비용이 드는 노드를 cost에 새로 담아왔는데 현재 위치한 노드 번호에 해당하는 비용이 배열에 기록된 값 distance[now]가 더 작았다면, 이미 방문한 적 있는 노드였다는 말과 같다. 값을 갱신할 수 없는 사례이기도 하다.# 동빈나 유튜브 36:52에 있음
            pass
        for i in graph[now]: # graph에는 이게 담겨 있다. graph[w] = (e, c) 즉, 노드 번호가 s면 e로 향하는 비용 c인 간선이 존재한다는 말. 노드 1에서 2, 3으로 가는 비용이 2, 4인 경우, graph[1] = [(2, 2), (3, 4)]가 있으니 노드 1에서 다른 노드로 가는 길이가 i만큼이 나올 것이다.
            temp_cost = cost + i[1] 

            if temp_cost < costs[i[0]]: # i[0]은 노드를 의미하는 값, 그 노드에 방문했던 적이 있다면 costs[i][0]값이 존재할 것이고, 새로 계산한 cost와 비교해보자.
                costs[i[0]] = temp_cost # 업데이트 하자
                heapq.heappush(q, (i[0], temp_cost)) # q배열에 (노드 번호, 새 비용)를 푸시한다.
            
                
# 다익스트라 수행


# 최단 거리 출력
# result = []
# for i in range(M+1):
#     if costs[i] == 0:
#         result.append(INF)
#     else:
#         result.append(costs[i])

# print(costs)
# print(result[end-1])

# if start > N or end > N:
#     pass
# elif N == 1:
#     print(0)
# elif M == 1:
#     print(graph[1][0][1])
# else:
    # dijkstra(start)
    # print(costs[end])

dijkstra(start)
print(costs[end])



# import sys
# from collections import defaultdict

# N = int(input())
# M = int(input())

# routes = defaultdict()

# for _ in range(M):
#     busin, busout, cost= map(int, sys.stdin.readline().split())
#     try:
#         routes[busin].append([busout, cost])
#     except:
#         routes[busin] = []
#         routes[busin].append([busout, cost])

# dep, arr = map(int, input().split(' '))


# # 출발지점 1에서 도착지점부터 5, 4, 3, 2 순으로 탐색
# costs = defaultdict()
# cost = 0

# def cost_search(route, whole_cost):
#     temp_cost = whole_cost
#     paths = routes[route]
#     # print('start paths', paths)
#     for path, cost in paths:
#         try:
#             if routes[path]:
#                 temp_cost += cost
#                 # print('try, nextpath, nextcost', path, whole_cost)
#                 cost_search(path, temp_cost)
            
#         except:
#             if path == arr:
#                 temp_cost += cost
#                 costs[temp_cost] = 1


# cost_search(1, 0)
# # print(costs)
# result = min(costs.keys())
# print(result)