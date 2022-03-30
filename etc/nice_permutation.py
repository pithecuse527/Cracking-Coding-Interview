import sys
input = sys.stdin.readline
N = int(input())

def promising(x):
    for i in range(1, (N//2)+1):
        if x[-i:] == x[2*-i:-i]:
            return False
    return True

def dfs(i, x):
    if i == N:
        print(x)
        return True
    for j in ['1', '2', '3']:
        if promising(x+j):
            if dfs(i+1, x+j):
                return True
    return False

for x in ['1', '2', '3']:
    if dfs(1, x):
        break
