import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

dp = [[1e9]*M for _ in range(N)]
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    dp[sy][sx] = 0
    visited = set()
    visited.add((sy, sx))

    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < N and 0 <= nx < M) or board[ny][nx] == 1 or (ny, nx) in visited:
                continue
            dp[ny][nx] = min(dp[ny][nx], dp[cy][cx]+1)
            q.append((ny, nx))
            visited.add((ny, nx))

sharks = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            sharks.append((y, x))
for sy, sx in sharks:
    bfs(sy, sx)

max_val = 0
for y in range(N):
    for x in range(M):
        max_val = max(max_val, dp[y][x])
print(max_val)