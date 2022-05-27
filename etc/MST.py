import sys
input = sys.stdin.readline
V, E = map(int, input().split())
parents = dict()
ranks = dict()
edges = []

def find(v):
    if v != parents[v]:  # path compression
        parents[v] = find(parents[v])

    return parents[v]

def union(u, v):
    u_root = find(u)
    v_root = find(v)

    if ranks[u_root] > ranks[v_root]:
        parents[v_root] = u_root
    else:
        parents[u_root] = v_root
        if ranks[u_root] == ranks[v_root]:
            ranks[v_root] += 1

for _ in range(E):
    edges.append(tuple(map(int, input().split())))
edges.sort(key=lambda x:x[2])

for v in range(1, V+1):
    parents[v] = v
    ranks[v] = 0

answer = 0
for edge in edges:
    u, v, w = edge
    if find(u) != find(v):
        union(u, v)
        answer += w
print(answer)