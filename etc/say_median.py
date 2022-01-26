import heapq
import sys

N = int(sys.stdin.readline())
min_heap = []
max_heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    if min_heap and min_heap[0] < -max_heap[0]:
        min_val = heapq.heappop(min_heap)
        max_val = heapq.heappop(max_heap)

        heapq.heappush(min_heap, -max_val)
        heapq.heappush(max_heap, -min_val)
    print(-max_heap[0])
