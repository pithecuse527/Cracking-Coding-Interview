from collections import deque
import sys
input = sys.stdin.readline
dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
        (2, -1), (2, 1), (1, -2), (1, 2)]

def bfs(sy, sx, ty, tx):
    q = deque()
    q.append((sy, sx))
    visited = [[-1 for j in range(N)] for i in range(N)]
    visited[sy][sx] = 0

    while q:
        cy, cx = q.popleft()
        if cy == ty and cx == tx:
            return visited[cy][cx]
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < N and 0 <= nx < N) or visited[ny][nx] != -1:
                continue
            visited[ny][nx] = visited[cy][cx] + 1
            q.append((ny, nx))
    return -1

for _ in range(int(input())):
    N = int(input())
    sy, sx = map(int, input().split())
    ty, tx = map(int, input().split())
    print(bfs(sy, sx, ty, tx))
