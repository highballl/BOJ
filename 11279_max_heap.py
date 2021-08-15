import heapq, sys
#input = sys.stdin.readline

N = int(input())
array = [int(sys.stdin.readline()) for _ in range(N)]
q = []
#count = 0
#result = 0
 
for i in range(N):
    #elem = int(input())
    #if elem == 0:
    if array[i] == 0:
        #count += 1
        #heapq.heappush(q, (0,0))
        if q == []:
            print(0)
        else:
            result = -heapq.heappop(q)[1]
            print(-result)
    elif array[i] != 0:    
        heapq.heappush(q, (-array[i], array[i]))
    # elif elem != 0:
        #heapq.heappush(q, (-elem, elem))



# while count > 0:
#     if q == []:
#         print(0)
#     else:
#         print(heapq.heappop(q))
#     count -= 1
    