from collections import defaultdict
from collections import defaultdict
import sys
input = sys.stdin.readline
INF = 1e9
V, E = map(int, input().split())
dist = [[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

ans = INF
for i in range(1, V+1):
    ans = min(ans, dist[i][i])
if ans == INF:
    print(-1)
else:
    print(ans)
