import heapq
import sys

input = sys.stdin.readline
INF = int(1e15)
n, p, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start, target_price):

    #초기화
    costs = [INF] * (n+1) # M개의 노드만큼 비용 정보를 담을 배열 초기화(INF)
    q = [] # heapq 를 위해 배열 준비
    heapq.heappush(q, (start, 0)) # 시작 노드, 비용 (비용=0, 자기자신일 때)
    costs[start] = 0 # 시작 노드에서의 비용 0을 따로 저장

    # 탐색
    # 큐가 존재한다면, 즉 비어있지 않다면
    while q : 
        # q의 가장 작은 값, 즉 비용이 가장 덜 드는 노드부터 탐색할 것이다 (현재 노드, 비용 순)
        now, cost = heapq.heappop(q) 
        
        # 처리된 적 있는 노드라면 스킵
        if costs[now] < cost: 
            continue
        for i in graph[now]: 
            if i[1] > target_price:
                if costs[i[0]] > cost + 1:
                    costs[i[0]] = cost + 1
                    # q배열에 (노드 번호, 새 비용)를 푸시한다.
                    heapq.heappush(q, (i[0], cost + 1)) 
            else:
                # i[0]은 노드를 의미하는 값, 그 노드에 방문했던 적이 있다면 costs[i][0]값이 존재할 것이고, 새로 계산한 cost와 비교해보자.
                if costs[i[0]] > cost : 
                    # 업데이트 하자
                    costs[i[0]] = cost 
                    # q배열에 (노드 번호, 새 비용)를 푸시한다.
                    heapq.heappush(q, (i[0], cost)) 

    if costs[n] > k:
        return False
    else:
        return True


def bisect_search():
    l, r = 0, 1000001
    ans = INF
    while l <= r:
        mid = (l + r) // 2
        pivot = dijkstra(1, mid)
        if pivot:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    
    if ans == INF:
        return -1
    else:
        return ans



print(bisect_search())
