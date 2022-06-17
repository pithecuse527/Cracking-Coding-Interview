import sys
input = sys.stdin.readline
N = int(input())    # the number of operators
INF = 1e9
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
max_value = -INF
min_value = INF

def dfs(accum, idx):
    global max_value, min_value
    if idx == N:
        max_value = max(max_value, accum)
        min_value = min(min_value, accum)
        return
    
    if ops[0]:
        ops[0] -= 1
        dfs(accum+nums[idx], idx+1)
        ops[0] += 1
    if ops[1]:
        ops[1] -= 1
        dfs(accum-nums[idx], idx+1)
        ops[1] += 1
    if ops[2]:
        ops[2] -= 1
        dfs(accum*nums[idx], idx+1)
        ops[2] += 1
    if ops[3]:
        ops[3] -= 1
        dfs(int(accum/nums[idx]), idx+1)
        ops[3] += 1

dfs(nums[0], 1)
print(max_value, min_value)