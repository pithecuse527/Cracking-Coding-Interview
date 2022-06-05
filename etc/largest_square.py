import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            dp[y][x] = 1

for y in range(1, N):
    for x in range(1, M):
        if board[y][x] == 1:
            dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1])+1

max_val = 0
for y in range(N):
    for x in range(M):
        max_val = max(max_val, dp[y][x])
print(max_val**2)
