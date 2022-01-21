N = int(input())

dp = [int(input())]
for _ in range(1, N):
    row = list(map(int, input().split()))
    next_dp = []
    for i in range(len(row)):
        if i == 0:
            next_dp.append(dp[i]+row[i])
        elif i == len(row)-1:
            next_dp.append(dp[i-1]+row[i])
        else:
            next_dp.append(max(dp[i-1]+row[i], dp[i]+row[i]))
    dp = next_dp

print(max(dp))
    