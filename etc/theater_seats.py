import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
fixed_seats = [int(input()) for _ in range(M)]
dp = [0] * (N+1)
dp[0], dp[1] = 1, 1

for i in range(2, N+1):
    dp[i] = dp[i-2]+dp[i-1]

answer = 1
if M > 0:
    prev = 0
    for i in range(M):
        answer *= dp[fixed_seats[i]-1-prev]
        prev = fixed_seats[i]
    answer *= dp[N-prev]
else:
    answer = dp[-1]
print(answer)
