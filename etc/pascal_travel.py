import sys
from collections import deque
input = sys.stdin.readline
dirs = [(1, 0), (0, 1)]

while True:
    N = int(input())
    if N == -1:
        break
    board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = 1
    
    for y in range(N):
        for x in range(N):
            if board[y][x] == 0 or dp[y][x] == 0:
                continue
            ny, nx = y+board[y][x], x+board[y][x]
            if ny < N:
                dp[ny][x] += dp[y][x]
            if nx < N:
                dp[y][nx] += dp[y][x]
    print(dp[-1][-1])
