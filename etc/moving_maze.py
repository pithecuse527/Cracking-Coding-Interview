from collections import deque
import sys
input = sys.stdin.readline

def bfs(board):
    q = deque()
    q.append((7, 0))
    visited = [[False]*8 for _ in range(8)]
    visited[7][0] = True
    dirs = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1),
             (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    while q:
        cy, cx = q.popleft()
        if board[cy][cx] == '#':
            continue
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < 8 and 0 <= nx < 8) or board[ny][nx] == '#':
                continue
            if ny == 0:
                return 1
            if not visited[ny-1][nx]:
                visited[ny-1][nx] = True
                q.append((ny-1, nx))
    return 0

board = [input() for _ in range(8)]
print(bfs(board))