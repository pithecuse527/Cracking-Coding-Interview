N = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    # if the int is too large, 
    # the space complexity would be O(N^2)
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[N])
