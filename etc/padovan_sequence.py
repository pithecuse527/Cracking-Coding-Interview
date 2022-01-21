def padovan(n):
    dp = [0, 1, 1]
    if n < 3:
        return dp[n]
    for i in range(3, n+1):
        dp.append(dp[i-2] + dp[i-3])
    return dp[n]

for _ in range(int(input())):
    print(padovan(int(input())))
