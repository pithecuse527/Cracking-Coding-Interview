from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    q = deque()
    q.append((0, 0, board[0][0]))
    dirs = [(1, 0), (0, 1)]
    dp = [[1e9]*M for _ in range(N)]
    dp[0][0] = 0
    # curr = board[0][0]

    while q:
        cy, cx, curr = q.popleft()
        for dy, dx in dirs:
            ny, nx = cy, cx
            for _ in range(curr):
                ny += dy
                nx += dx
                if not (0 <= ny < N and 0 <= nx < M):
                    continue
                if dp[ny][nx] > dp[cy][cx]+1:
                    dp[ny][nx] = dp[cy][cx]+1
                    q.append((ny, nx, board[ny][nx]))
    return dp[-1][-1]
print(bfs())
