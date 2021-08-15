import heapq, sys
input = sys.stdin.readline
INF = int(1e9)
 
V, E = map(int, input().split()) # 노드의 개수 v, 간선의 개수 e
start = int(input()) # 시작점
graph = [[] for i in range(V+1)] # v개의 노드만큼 그래프 배열 만들어두기
distance = [INF] * (V+1) # v개의 노드만큼 infinite로 거리 정보를 담을 배열 초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):

    #초기화
    q = [] # heapq 를 위해 배열 준비
    heapq.heappush(q, (0, start)) # 거리, 시작 노드 (거리=0, 자기자신일 때)
    distance[start] = 0 # 시작 노드에서의 거리 0을 따로 저장

    # 탐색
    while q : # 큐가 존재한다면, 즉 비어있지 않다면
        dist, now = heapq.heappop(q) # q의 가장 작은 값, 즉 최단 거리가 가장 짧은 노드부터 탐색할 것이다 (거리, 현재 노드 순)
        if distance[now] < dist: # 최단 거리가 가장 짧은 노드를 dist에 새로 담아왔는데 현재 위치한 노드 번호에 해당하는 거리가 배열에 기록된 값 distance[now]가 더 작았다면, 이미 방문한 적 있는 노드였다는 말과 같다. 값을 갱신할 수 없는 사례이기도 하다.# 동빈나 유튜브 36:52에 있음
            continue
        for i in graph[now]: # graph에는 이게 담겨 있다. graph[u] = (v, w) 즉, 노드 번호가 u면 v로 향하는 가중치 w인 간선이 존재한다는 말. 노드 1에서 2, 3으로 가는 가중치가 2, 4인 경우, graph[1] = [(2, 2), (3, 4)]가 있으니 노드 1에서 다른 노드로 가는 길이가 i만큼이 나올 것이다.
            cost = dist + i[1] 
            # 출발지점에서 현재 노드까지 이르는 거리의 총합 cost는 dist(현재 노드에서 최단 거리 목적지로 향할 때의 거리값) + i[1]은 (2, 2), (3, 4)에서 간선의 가중치 2, 4에 해당하는 값이다.
            # 예 : graph = [[0],[(2,2),(3,4)]]
            # print(graph[1][0][1]) # 2
            # print(graph[1][1][1]) # 4
            if cost < distance[i[0]]: # i[0]은 노드를 의미하는 값, 그 노드에 방문했던 적이 있다면 distance[i][0]값이 존재할 것이고, 새로 계산한 cost와 비교해보자.
                distance[i[0]] = cost # 업데이트 하자
                heapq.heappush(q, (cost, i[0])) # q배열에 (새 거리, 노드 번호)를 푸시한다.
    
# 다익스트라 수행
dijkstra(start)

# 최단 거리 출력
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    elif distance[i] == 0:
        print(0)
    else:
        print(distance[i])


