import sys, heapq
 
n = int(input())
array = list(int(sys.stdin.readline().strip()) for _ in range(n))
result = []

print(array)
for i in range(0, n):
    if array[i] == 0 and len(result) == 0:
        print(0)
    elif array[i] != 0 :
        heapq.heappush(result, array[i])
    elif array[i] == 0:
        temp = heapq.heappop(result)
        print(temp)



# for i in range(0, n):
#     if array[i] == 0 and len(result) == 0:
#         print(0)
#     elif array[i] != 0:
#         result[array[i]] = array[i]
#     elif array[i] == 0 and len(result) !=0 :
#         print(min(result.keys()))
        
        

