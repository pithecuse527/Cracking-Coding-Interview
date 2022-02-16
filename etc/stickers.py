import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    arr = [[0]*100000 for _ in range(2)]
    dp = [[0]*100000 for _ in range(2)]
    row = list(map(int, input().split()))
    for i in range(N):
        arr[0][i] = row[i]
    row = list(map(int, input().split()))
    for i in range(N):
        arr[1][i] = row[i]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = arr[0][1] + dp[1][0]
    dp[1][1] = arr[1][1] + dp[0][0]

    for i in range(2, N):
        dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2])
    answer = max(dp[0][N-1], dp[1][N-1])
    print(answer)
