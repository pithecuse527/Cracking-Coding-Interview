dp = [[0]*101 for _ in range(101)]

def combi_dp(n, m):
    for i in range(n+1):
        for j in range(m+1):
            if i == j or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
    return dp[n][m]

N, M = map(int, input().split())
print(combi_dp(N, M))
