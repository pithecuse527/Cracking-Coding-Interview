N = int(input())
S = [0]

for _ in range(N):
    S.append(int(input()))

if N < 2:
    print(S[1])
    exit()

dp = [0]
dp.append(S[1])
dp.append(S[1]+S[2])

for i in range(3, N+1):
    dp.append(max(dp[i-2]+S[i], dp[i-3]+S[i-1]+S[i]))
print(dp[-1])
