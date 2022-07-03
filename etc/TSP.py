import sys
input = sys.stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(1 << N-1) for _ in range(N)]

def dfs(s, route):
    if dp[s][route] != 0:
        return dp[s][route]
    
    if route == (1 << (N-1))-1:
        return W[s][0] if W[s][0] else float('inf')
    
    min_route = float('inf')
    for n in range(1, N):
        if not W[s][n] or (route & (1 << n-1)):
            continue
        dist = W[s][n] + dfs(n, route | (1 << (n-1)))
        min_route = min(min_route, dist)
    dp[s][route] = min_route
    return min_route
print(dfs(0, 0))
