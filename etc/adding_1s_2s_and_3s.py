T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, N+1):
        for s in [1,2,3]:
            if i - s > 0:
                dp[i] += dp[i-s]
    print(dp[N])
    