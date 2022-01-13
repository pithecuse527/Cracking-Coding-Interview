import heapq

N, M = map(int, input().split())

adj = [list() for _ in range(N+1)]
inner_degree = [0 for _ in range(N+1)]
result = []
heap = []

# graph setting
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)  # x -> y

    # point by something means the inner degree should be increased
    inner_degree[y] += 1

# initial heap setting with 0 inner degree
for i in range(1, len(inner_degree)):
    if inner_degree[i] == 0:
        heapq.heappush(heap, i)

# heappop
while heap:
    problem = heapq.heappop(heap)
    result.append(problem)
    for p in adj[problem]:
        inner_degree[p] -= 1
        if inner_degree[p] == 0:
            heapq.heappush(heap, p)

for p in result:
    print(p, end=' ')
print()
