import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for j in range(N)] for i in range(N)]
dp[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if board[i][j] == 1:
            continue
        if j-1 >= 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        if i-1 >= 0:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if i-1 >= 0 and j-1 >= 0 and board[i-1][j] != 1 and board[i][j-1] != 1:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
print(dp[N-1][N-1][0]+dp[N-1][N-1][1]+dp[N-1][N-1][2])
