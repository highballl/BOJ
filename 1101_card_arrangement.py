import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

def not_zero_cnt(cards):
    not_z_cnt = 0
    elems = []
    for idx, card in enumerate(cards):
        if card == 0:
            continue
        else:
            not_z_cnt += 1
            elems.append(idx)
    return not_z_cnt, elems

def main():
    nz_heap_list = []
    for i in range(n):
        cards = list(map(int, input().split()))
        not_z_cnt, elems = not_zero_cnt(cards)
        heapq.heappush(nz_heap_list, [-not_z_cnt, elems])

    heapq.heappop(nz_heap_list)[0]

    cnt = 0
    visited = [False] * m 

    not_zero_list = nz_heap_list
    for nzlist in not_zero_list:
        if -nzlist[0] > 1:
            cnt += 1
        if -nzlist[0] == 1:
            elem = nzlist[1][0]
            if visited[elem] == False:
                visited[elem] = True
            elif visited[elem] == True:
                cnt += 1
    return cnt

print(main())

