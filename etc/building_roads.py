import sys
input = sys.stdin.readline
N, M = map(int, input().split())
parent = dict()
rank = dict()
V = []
E = []

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

for _ in range(N):
    V.append(tuple(map(int, input().split())))

for i in range(N):
    for j in range(i+1, N):
        dist = ((V[i][0]-V[j][0])**2+(V[i][1]-V[j][1])**2)**0.5
        E.append((V[i], V[j], dist))
E.sort(key=lambda x:x[2])

for i in range(N):
    parent[V[i]] = V[i]
    rank[V[i]] = 0

for _ in range(M):
    u, v = map(int, input().split())
    union(V[u-1], V[v-1])

cost = 0
for edge in E:
    u, v, w = edge
    if find(u) != find(v):
        union(u, v)
        cost += w
print('%.2f' % cost)
