N = int(input())
sequence = list(map(int, input().split()))

dp = []
for i in range(N):
    dp.append(1)
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j]+1)
    print(dp)
print("result:", max(dp))
