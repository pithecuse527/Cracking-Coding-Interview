import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N, S, P = map(int, input().split())
graph = [list() for _ in range(N+1)]

def dfs(current, visited, current_depth, depths):
    if 1 <= current <= S:
        depths.append(current_depth)
        return
    visited.add(current)
    for next in graph[current]:
        if next not in visited:
            # visited.add(next)
            dfs(next, visited, current_depth+1, depths)

for _ in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

depths = []
dfs(P, set(), 0, depths)
depths.sort()
# print(depths)
print(N-depths[0]-depths[1]-1)