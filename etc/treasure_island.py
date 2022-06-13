from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [input() for _ in range(N)]
answer = 0

def bfs(sy, sx):
    global answer
    q = deque()
    q.append((sy, sx))
    visited = [[-1]*M for _ in range(N)]
    visited[sy][sx] = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    max_len = 0
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < N and 0 <= nx < M) or visited[ny][nx] != -1 or grid[ny][nx] == 'W':
                continue
            visited[ny][nx] = visited[cy][cx] + 1
            q.append((ny, nx))
            max_len = max(max_len, visited[ny][nx])
    answer = max(max_len, answer)

for y in range(N):
    for x in range(M):
        if grid[y][x] == 'L':
            bfs(y, x)
print(answer)
