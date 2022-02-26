import heapq

N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]
classes.sort()  # sort by start time

q = []
for start, end in classes:
    if not q:
        q.append(end)
        continue

    if q[0] > start:
        heapq.heappush(q, end)
    else:
        heapq.heappop(q)
        heapq.heappush(q, end)
print(len(q))