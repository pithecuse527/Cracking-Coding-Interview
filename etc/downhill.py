import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M, N = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(y, x, dp):
    if (y, x) == (M-1, N-1):
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    for dy, dx in dirs:
        ny, nx = dy+y, dx+x
        if 0 <= ny < M and 0 <= nx < N and hills[y][x] > hills[ny][nx]:
            dp[y][x] += dfs(ny, nx, dp)
    return dp[y][x]
print(dfs(0, 0, dp))
