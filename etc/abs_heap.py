import heapq, sys
input = sys.stdin.readline
N = int(input())

hq = []
for _ in range(N):
    item = int(input())
    if item != 0:
        item_abs = abs(item)
        heapq.heappush(hq, (item_abs, item))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
