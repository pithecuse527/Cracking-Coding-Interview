import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
sums = set()

def dfs(accum, idx):
    if idx == N:
        sums.add(accum)
        return
    
    dfs(accum+S[idx], idx+1)
    dfs(accum, idx+1)

dfs(0, 0)
# print(sorted(sums))
for i in range(1, max(sums)+2):
    if i not in sums:
        print(i)
        exit()
