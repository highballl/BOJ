import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
 
N, M = map(int, input().split()) # 도시의 수 N, 간선의 수 M

graph = [[] for i in range(N+1)] # M개의 노드(버스의 수)만큼 그래프 배열 만들어두기

for _ in range(M):
    s, e, c = map(int, input().split()) # start, end, cost
    graph[s].append((e, c))
    graph[e].append((s, c))


v_1, v_2 = map(int, input().split()) # 지나야 하는 노드 2개


def dijkstra(start, end):

    #초기화
    costs = [INF] * (N+1) # M개의 노드만큼 비용 정보를 담을 배열 초기화(INF)

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

            if temp_cost < costs[i[0]]: # i[0]은 노드를 의미하는 값, 그 노드에 방문했던 적이 있다면 costs[i][0]값이 존재할 것이고, 새로 계산한 cost와 비교해보자.
                costs[i[0]] = temp_cost # 업데이트 하자
                heapq.heappush(q, (i[0], temp_cost)) # q배열에 (노드 번호, 새 비용)를 푸시한다.
    
    return costs[end]
                
# 다익스트라 수행
# 입력 조건을 지키자
if v_1 == v_2 or v_1 == N or v_2 == 1:
    print(-1)

try:
    s_v_1 = dijkstra(1, v_1)
    v_1_v_2 = dijkstra(v_1, v_2)
    v_2_e = dijkstra(v_2, N)
        
    path_1 = s_v_1 + v_1_v_2 + v_2_e

    s_v_2 = dijkstra(1, v_2)
    v_2_v_1 = dijkstra(v_2, v_1)
    v_1_e = dijkstra(v_1, N)

    path_2 = s_v_2 + v_2_v_1 + v_1_e

    result = min(path_1, path_2)

    if result >= INF:
        print(-1)
    else:
        print(result)
except:
    print(-1)

