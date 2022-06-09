from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(board):
    q = deque()
    q.append((0, 0))
    visited = set()
    visited.add((0, 0))

    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < N and 0 <= nx < M) or (ny, nx) in visited:
                continue
            if board[ny][nx] >= 1:
                board[ny][nx] += 1
            else:
                visited.add((ny, nx))
                q.append((ny, nx))

    return len(visited)

cnt = 0
while bfs(board) != N*M:
    cnt += 1

    for y in range(N):
        for x in range(M):
            if board[y][x] >= 3:
                board[y][x] = 0
            elif board[y][x] == 2:
                board[y][x] = 1
print(cnt)
