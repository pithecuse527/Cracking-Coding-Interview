import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [[0]*(N+1) for _ in range(K+1)]
for x in range(1, N+1):
    dp[1][x] = 1

for y in range(2, K+1):
    dp[y][1] = y
    for x in range(2, N+1):
        dp[y][x] = (dp[y-1][x]+dp[y][x-1]) % 1000000000
print(dp[-1][-1])
