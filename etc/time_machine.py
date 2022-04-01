import sys
input = sys.stdin.readline
INF = 1e9
N, M = map(int, input().split())
edges = []
dist = [INF]*(N+1)

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

def bellman_ford(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            c, n, e = edges[j]
            if dist[c] != INF and dist[n] > dist[c]+e:
                dist[n] = dist[c]+e
                if i == N-1:
                    return True
    return False

neg_cycle = bellman_ford(1)
if neg_cycle:
    print(-1)
else:
    for n in range(2, N+1):
        if dist[n] != INF:
            print(dist[n])
        else:
            print(-1)
