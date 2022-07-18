import sys
input = sys.stdin.readline
N = int(input())
consulting = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
def dfs(idx, accum):
    global ans
    if idx == N:
        ans = max(ans, accum)
        return
    
    if idx+consulting[idx][0] <= N:
        dfs(idx+consulting[idx][0], accum+consulting[idx][1])
    dfs(idx+1, accum)
dfs(0, 0)
print(ans)
