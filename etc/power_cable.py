import sys
input = sys.stdin.readline
N = int(input())
conn = [tuple(map(int, input().split())) for _ in range(N)]
conn.sort(key=lambda x:x[0])
dp = [1]*(N+1)

for i in range(1, N+1):
    for j in range(1, i):
        if conn[j-1][1] < conn[i-1][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))