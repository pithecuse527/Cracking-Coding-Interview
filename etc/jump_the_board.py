from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(0, 1), (1, 0)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for y in range(N):
    for x in range(N):
        if board[y][x] == 0:
            continue
        for dy, dx in dirs:
            ny, nx = board[y][x]*dy+y, board[y][x]*dx+x
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            dp[ny][nx] += dp[y][x]
print(dp[-1][-1])
