import heapq
import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    data = int(sys.stdin.readline())
    if data == 0:
        if lst:
            print(heapq.heappop(lst))
        else:
            print(0)
    else:
        heapq.heappush(lst, data)
