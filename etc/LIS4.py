N = int(input())
sequence = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j]+1)

target_len = max(dp)
print(target_len)

ans = []
for i in range(N-1, -1, -1):
    if dp[i] == target_len:
        ans.append(sequence[i])
        target_len -= 1
ans.reverse()
print(*ans)
