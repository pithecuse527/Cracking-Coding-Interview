import heapq
INF = 1e9

V, E = map(int, input().split())
K = int(input())

adj_mtx = [list() for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_mtx[u].append((w, v))   # cost and adj. node

def dijkstra(adj_mtx, start):
    distance = [INF for _ in range(V+1)]
    distance[start] = 0
    q = [(0, start)]

    while q:
        curr_node_cost, curr_node_num = heapq.heappop(q)
        if distance[curr_node_num] < curr_node_cost:
            continue
        for adj_cost, adj_node_num in adj_mtx[curr_node_num]:
            cost = adj_cost + distance[curr_node_num]
            if cost < distance[adj_node_num]:
                distance[adj_node_num] = cost
                heapq.heappush(q, (cost, adj_node_num))
    return distance

distance = dijkstra(adj_mtx, K)
for i in range(1, V+1):
    if distance[i] != 1e9:
        print(distance[i])
    else:
        print('INF')
