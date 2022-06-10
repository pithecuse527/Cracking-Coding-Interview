import sys
input = sys.stdin.readline
N = int(input())
visited = [[False]*N for _ in range(N)]
mtx = [list(map(int, input().split())) for _ in range(N)]
min_val = 1e9

def dfs(depth):
    global min_val
    if depth == N:
        score1, score2 = 0, 0
        for i in range(N-1):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    score1 += mtx[i][j]+mtx[j][i]
                elif not visited[i] and not visited[j]:
                    score2 += mtx[i][j]+mtx[j][i]
        min_val = min(min_val, abs(score1-score2))
        return
    
    visited[depth] = True
    dfs(depth+1)
    visited[depth] = False
    dfs(depth+1)
dfs(0)
print(min_val)