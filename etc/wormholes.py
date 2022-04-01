import sys
input = sys.stdin.readline
INF = 1e9

def bellman_ford(start, N, edges):
    dist = [INF]*(N+1)
    dist[start] = 0
    for i in range(N):
        for c, n, e in edges:
            if dist[n] > dist[c]+e:
                dist[n] = dist[c]+e
                if i == N-1:
                    return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
    
    if bellman_ford(1, N, edges):
        print('YES')
    else:
        print('NO')
