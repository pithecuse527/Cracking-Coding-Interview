import sys
input = sys.stdin.readline
dirs = [[(-1, 0), (0, -1)], [(-1, 0), (0, 1)], 
        [(1, 0), (0, -1)], [(1, 0), (0, 1)]]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

ans = 0
def dfs(y, x, accum):
    global ans, visited
    if x == M:
        x = 0
        y += 1

    if y == N:
        ans = max(ans, accum)
        return

    if not visited[y][x]:
        for d in dirs:
            ny1, nx1 = d[0][0]+y, d[0][1]+x
            ny2, nx2 = d[1][0]+y, d[1][1]+x

            if (0 <= ny1 < N and 0 <= nx1 < M and 0 <= ny2 < N and 0 <= nx2 < M and not visited[ny1][nx1] and not visited[ny2][nx2]):
                visited[y][x] = True
                visited[ny1][nx1] = True
                visited[ny2][nx2] = True
                next_accum = accum + 2*board[y][x] + board[ny1][nx1] + board[ny2][nx2]
                dfs(y, x+1, next_accum)
                visited[y][x] = False
                visited[ny1][nx1] = False
                visited[ny2][nx2] = False
    dfs(y, x+1, accum)
dfs(0, 0, 0)
print(ans)
