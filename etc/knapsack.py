N, K = map(int, input().split())

stuffs = []
weights = [0]
values = [0]
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# dp matrix ready
dp = [[0 for y in range(K+1)] for x in range(N+1)]

# dp running
for i in range(1, N+1):
    for j in range(1, K+1):
        # case1 (if the maximum weight is lower than current stuff)
        if j < weights[i]:  
            dp[i][j] = dp[i-1][j]
        # case2
        else:       # choose whether take the stuff or not 
            dp[i][j] = max(dp[i-1][j-weights[i]]+values[i], dp[i-1][j])

# final result
print(dp[N][K])
