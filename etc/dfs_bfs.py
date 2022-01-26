from collections import deque
N, M, V = map(int, input().split())

adj_mtx = [list() for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj_mtx[x].append(y)
    adj_mtx[y].append(x)

for e in adj_mtx:
    e.sort()

dfs_result = []
dfs_visited = set()
def dfs(n):
    dfs_result.append(n)
    dfs_visited.add(n)

    for c in adj_mtx[n]:
        if c not in dfs_visited:
            dfs(c)

bfs_result = []
bfs_visited = set()
def bfs(n):
    q = deque([n])
    while q:
        front = q.popleft()
        if front not in bfs_visited:
            bfs_result.append(front)
            bfs_visited.add(front)
            for c in adj_mtx[front]:
                if c not in bfs_visited:
                    q.append(c)

dfs(V)
bfs(V)
for c in dfs_result:
    print(c, end=" ")

print()
for c in bfs_result:
    print(c, end=" ")
print()