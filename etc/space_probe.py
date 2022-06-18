import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(N)]

answer = 1e9
def dfs(i, accum, visited):
    global answer
    if len(visited) == N:
        answer = min(answer, accum)
        return
    
    for j in range(N):
        if j not in visited:
            visited.add(j)
            dfs(j, accum+dist[i][j], visited)
            visited.discard(j)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][k]+dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k]+dist[k][j]
dfs(K, 0, set())
print(answer)