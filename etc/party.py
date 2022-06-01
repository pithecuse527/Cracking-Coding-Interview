import sys, heapq
input = sys.stdin.readline
INF = 1e9
N, M, X = map(int, input().split())
graph = [list() for _ in range(N+1)]

def dijkstra(start, end):
    distance = [INF]*(N+1)
    distance[start] = 0
    hq = [(0, start)]

    while hq:
        dist, curr = heapq.heappop(hq)
        if distance[curr] < dist:
            continue
        for n, w in graph[curr]:
            cost = w+dist
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(hq, (cost, n))
    return distance[end]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

max_len = 0
for i in range(1, N+1):
    max_len = max(max_len, dijkstra(i, X)+dijkstra(X, i))
print(max_len)
