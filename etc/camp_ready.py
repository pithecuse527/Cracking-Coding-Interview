import sys
input = sys.stdin.readline
N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))

cnt = 0
def dfs(selected, idx):
    global cnt
    if idx >= N:
        if len(selected) > 1 and L <= sum(selected) and max(selected)-min(selected) >= X:
            # print(selected)
            cnt += 1
        return
    
    selected.append(problems[idx])
    if sum(selected) <= R:
        dfs(selected, idx+1)
    selected.pop()
    dfs(selected, idx+1)

dfs(list(), 0)
print(cnt)
