import sys
input = sys.stdin.readline
N, S = map(int, input().split())
sequence = list(map(int, input().split()))

cnt = 0

def dfs(sub_sum, idx):
    global cnt
    if idx >= N:
        return
    
    sub_sum += sequence[idx]
    if sub_sum == S:
        cnt += 1

    dfs(sub_sum, idx+1)
    dfs(sub_sum-sequence[idx], idx+1)
dfs(0, 0)
print(cnt)