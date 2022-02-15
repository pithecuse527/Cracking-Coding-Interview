N = int(input())

dp = [0]*5001
dp[3] = 1
dp[5] = 1
for i in range(4, N+1):
    if i-5 > 0 and dp[i-5] != 0:
        dp[i] = dp[i-5]+1
    elif i-3 > 0 and dp[i-3] != 0:
        dp[i] = dp[i-3]+1
    
if dp[N] == 0:
    print(-1)
else:
    print(dp[N])
