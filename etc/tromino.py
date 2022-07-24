N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_value = 0

def dfs(cy, cx, accum, cnt, visited):
    global max_value
    if cnt == 3:
        max_value = max(max_value, accum)
        return
    
    for dy, dx in dirs:
        ny, nx = cy+dy, cx+dx
        if not (0 <= ny < N and 0 <= nx < M) or visited[ny][nx]:
            continue
        
        visited[ny][nx] = True
        dfs(ny, nx, accum+board[ny][nx], cnt+1, visited)
        visited[ny][nx] = False

visited = [[False]*M for _ in range(N)]
for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(y, x, board[y][x], 1, visited)
        visited[y][x] = False
print(max_value)
