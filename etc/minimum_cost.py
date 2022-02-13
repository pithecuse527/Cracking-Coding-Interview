import heapq
INF = 1e9

N = int(input())
M = int(input())
adj_mtx = [list() for _ in range(N+1)]
for _ in range(M):
    c1, c2, cost = map(int, input().split())
    adj_mtx[c1].append((cost, c2))
start, end = map(int, input().split())
    
def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = [(0, start)]

    while q:
        curr_city_cost, curr_city = heapq.heappop(q)
        if distance[curr_city] < curr_city_cost:
            continue
        for dist_, adj_city in adj_mtx[curr_city]:
            cost = dist_ + distance[curr_city]
            if distance[adj_city] > cost:
                distance[adj_city] = cost
                heapq.heappush(q, (cost, adj_city))
    return distance
distance = dijkstra(start)
print(distance[end])