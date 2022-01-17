s1 = input()
s2 = input()

s1_len = len(s1)
s2_len = len(s2)

dp = [[0] * (s2_len+1) for x in range(s1_len+1)]

for i in range(1, s1_len+1):
    for j in range(1, s2_len+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
