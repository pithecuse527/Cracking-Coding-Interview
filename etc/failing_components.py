import heapq
import sys
input = sys.stdin.readline
INF = 1e9
T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())
    dependency = [list() for _ in range(n+1)]
    path = [INF for _ in range(n+1)]
    path[c] = 0
    for i in range(d):
        a, b, s = map(int, input().split())
        dependency[b].append((a, s))
    
    q = [(c, 0)]
    while q:
        c_node, c_distance = heapq.heappop(q)
        if path[c_node] < c_distance:
            continue

        for adj_node, adj_distance in dependency[c_node]:
            cost = c_distance + adj_distance
            if path[adj_node] > cost:
                path[adj_node] = cost
                heapq.heappush(q, (adj_node, cost))
    
    # find the number of infected computers and its taken time
    cnt = 0
    time = 0
    for i in range(1, n+1):
        if path[i] == INF:
            continue
        cnt += 1
        time = max(time, path[i])
    print(cnt, time)
    