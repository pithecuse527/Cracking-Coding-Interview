N = int(input())
dp = [0, 0]

for i in range(2, N+1):
    dp.append(dp[i-1]+1)
    if i % 2 == 0:
        dp[i] = min(1+dp[i//2], dp[i])
    if i % 3 == 0:
        dp[i] = min(1+dp[i//3], dp[i])
print(dp[-1])
