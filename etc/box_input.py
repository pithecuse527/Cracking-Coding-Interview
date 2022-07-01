import sys
input = sys.stdin.readline
N = int(input())
boxes = list(map(int, input().split()))
dp = [1]*N

for i in range(N-1):
    for j in range(i+1, N):
        if boxes[i] < boxes[j] and dp[j] < dp[i]+1:
            dp[j] = dp[i]+1
print(max(dp))
