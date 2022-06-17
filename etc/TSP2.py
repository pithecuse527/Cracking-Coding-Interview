import sys
input = sys.stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
found_route = 1e9

def promising(accum):
    if found_route <= accum:
        return False
    return True

def dfs(start, curr, visited, accum):
    global found_route
    if len(visited) == N:
        if W[curr][start] != 0 and found_route > accum+W[curr][start]:
            found_route = accum+W[curr][start]
        return
    for i in range(N):
        if W[curr][i] != 0 and i not in visited and promising(accum+W[curr][i]):
            visited.add(i)
            dfs(start, i, visited, accum+W[curr][i])
            visited.discard(i)

for start in range(N):
    dfs(start, start, set([start]), 0)
print(found_route)