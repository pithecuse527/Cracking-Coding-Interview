import sys, heapq
input = sys.stdin.readline
INF = 1e9
N, E = map(int, input().split())
graph = [list() for _ in range(N+1)]

def dijkstra(start):
    distances = [INF]*(N+1)
    distances[start] = 0
    hq = [(0, start)]

    while hq:
        curr_cost, curr = heapq.heappop(hq)
        if distances[curr] < curr_cost:
            continue
        for next_, dist in graph[curr]:
            cost = curr_cost + dist
            if cost < distances[next_]:
                distances[next_] = cost
                heapq.heappush(hq, (cost, next_))
    return distances

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
v1, v2 = map(int, input().split())

path1 = dijkstra(1)[v1]+dijkstra(v1)[v2]+dijkstra(v2)[N]
path2 = dijkstra(1)[v2]+dijkstra(v2)[v1]+dijkstra(v1)[N]
print(-1 if min(path1, path2) >= INF else min(path1, path2))
