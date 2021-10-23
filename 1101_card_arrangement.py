import heapq
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n, m = map(int, input().split())

def not_zero_cnt(cards):
    not_z_cnt = 0
    elems = []
    for idx, card in enumerate(cards):
        if card == 0:
            continue
        elif card != 0:
            not_z_cnt += 1
            elems.append(idx)
    return not_z_cnt, elems


def get_list():
    nz_heap_list = []
    nz_normal_list = []
    check = defaultdict(int)
    for _ in range(n):
        cards = list(map(int, input().split()))
        not_z_cnt, elems = not_zero_cnt(cards)
        if [-not_z_cnt, elems] in nz_normal_list:
            idx = nz_normal_list.index([-not_z_cnt, elems])
            check[idx] += 1
        heapq.heappush(nz_heap_list, [-not_z_cnt, elems])
        nz_normal_list.append([-not_z_cnt, elems])

    is_max = -nz_heap_list[0][0]
    is_max_idx = nz_normal_list.index(nz_heap_list[0])
    
    
    if check and not check[is_max_idx]:
        sorted_check = sorted(check.items(), key=lambda item: item[1], reverse=True)[0]
        
        remove_idx = sorted_check[0]

        nz_normal_list = deque(nz_normal_list)
        nz_normal_list.rotate(-remove_idx)
        is_max_2 = -nz_normal_list.popleft()[0]
        

        if is_max > is_max_2 : 
            heapq.heappop(nz_heap_list)
            return nz_heap_list
        return nz_normal_list

    else:
       # Joker Box
        heapq.heappop(nz_heap_list)
        return nz_heap_list


def main():
    nz_list = get_list()
    cnt = 0
    visited = [False] * m 

    for nzlist in nz_list:
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

