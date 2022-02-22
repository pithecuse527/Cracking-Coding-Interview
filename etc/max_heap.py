import heapq, sys
input = sys.stdin.readline
N = int(input())

hq = []
for _ in range(N):
    item = int(input())
    if item == 0:
        if hq:
            print(-(heapq.heappop(hq)))
        else:
            print(0)
    else:
        heapq.heappush(hq, -item)
