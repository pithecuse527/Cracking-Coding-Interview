import sys
input = sys.stdin.readline
R, C, K = map(int, input().split())
board = [input() for _ in range(R)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*C for _ in range(R)]

answer = 0
def dfs(cy, cx, cnt):
    global answer, visited
    if cnt == K:
        if (cy, cx) == (0, C-1):
            answer += 1
        return
    
    for dy, dx in dirs:
        ny, nx = cy+dy, cx+dx
        if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx] and board[ny][nx] != 'T':
            visited[ny][nx] = True
            dfs(ny, nx, cnt+1)
            visited[ny][nx] = False
visited[R-1][0] = True
dfs(R-1, 0, 1)
print(answer)
