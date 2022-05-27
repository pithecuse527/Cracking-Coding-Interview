import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
edges = []
parent = dict()
rank = dict()

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    u_root = find(u)
    v_root = find(v)

    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    else:
        parent[v_root] = u_root
        if rank[u_root] == rank[v_root]:
            rank[u_root] += 1

for _ in range(M):
    edges.append(tuple(map(int, input().split())))
edges.sort(key=lambda x:x[2])

for v in range(1, N+1):
    parent[v] = v
    rank[v] = 0

total_min_cost = 0
for edge in edges:
    u, v, w = edge
    if find(u) != find(v):
        union(u, v)
        total_min_cost += w
print(total_min_cost)
