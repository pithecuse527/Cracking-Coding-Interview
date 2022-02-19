import copy
N, M = map(int, input().split())
array = [[0]*(N+1)]
for _ in range(N):
    array.append([0]+list(map(int, input().split())))

query = [list(map(int, input().split())) for _ in range(M)]

# dp ready
dp = [[0]*1025 for _ in range(1025)]
dp[1][1] = array[1][1]
for i in range(2, N+1):
    dp[1][i] = dp[1][i-1]+array[1][i]
    dp[i][1] = dp[i-1][1]+array[i][1]

# bottom up (calculate the prefix sum)
for y in range(1, N):
    for x in range(1, N):
        dp[y+1][x+1] = dp[y+1][x]+dp[y][x+1]+array[y+1][x+1]-dp[y][x]

# find the answer with prefix sum
for y1, x1, y2, x2 in query:
    ans = dp[y2][x2]-dp[y1-1][x2]-dp[y2][x1-1]+dp[y1-1][x1-1]
    print(ans)
