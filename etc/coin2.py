import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [10001] * (K+1)
dp[0] = 0
coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
