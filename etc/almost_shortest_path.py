import heapq
from collections import deque
import sys
input = sys.stdin.readline
INF = 1e9

def dijkstra(adj_points, dropped, N, S):
    distance = [INF] * N
    q = [(S, 0)]
    distance[S] = 0

    while q:
        p, p_d = heapq.heappop(q)
        if distance[p] < p_d:
            continue
        for c, c_d in adj_points[p]:
            cost = p_d + c_d
            if cost < distance[c] and not dropped[p][c]:
                heapq.heappush(q, (c, cost))
                distance[c] = cost
    return distance

def bfs(rev_points, min_distance, S, D, N):
    q = deque([D])
    dropped = [[False]*N for _ in range(N)]
    while q:
        front = q.popleft()
        if front == S:
            continue
        for prev, cost in rev_points[front]:
            if dropped[prev][front]:
                continue
            if min_distance[front] == min_distance[prev]+cost:
                dropped[prev][front] = True
                q.append(prev)
    return dropped

while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    S, D = map(int, input().split())

    adj_points = [list() for _ in range(N)]
    rev_points = [list() for _ in range(N)]
    dropped = [[False]*N for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        adj_points[U].append((V, P))
        rev_points[V].append((U, P))
    min_distance = dijkstra(adj_points, dropped, N, S)
    dropped = bfs(rev_points, min_distance, S, D, N)
    min_distance = dijkstra(adj_points, dropped, N, S)
    if min_distance[D] == INF:
        print(-1)
    else:
        print(min_distance[D])
