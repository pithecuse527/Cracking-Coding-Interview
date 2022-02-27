from collections import deque
import heapq, sys
input = sys.stdin.readline
INF = 1e9

N = int(input())
M = int(input())
adj_mtx = [list() for _ in range(N+1)]
rev_adj_mtx = [list() for _ in range(N+1)]
for _ in range(M):
    c1, c2, cost = map(int, input().split())
    adj_mtx[c1].append((cost, c2))
    rev_adj_mtx[c2].append((cost, c1))
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

def bfs_find(start, end, distance):
    path = [end]
    q = deque([(end, distance[end])])
    visited = set()
    visited.add(end)
    while q:
        node_to, min_cost = q.popleft()
        if node_to == start:    # should consider this (the breaking point)
            break
        for cost, node_from in rev_adj_mtx[node_to]:
            if distance[node_from]+cost == min_cost and node_from not in visited:
                path.append(node_from)
                q.append((node_from, distance[node_from]))
                visited.add(node_from)
                break
    return path

distance = dijkstra(start)
print(distance[end])
path = bfs_find(start, end, distance)
print(len(path))
while path: print(path.pop(), end=' ')
print()