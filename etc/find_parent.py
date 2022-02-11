import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj = [list() for _ in range(N+1)]
parent = [-1] * (N+1)

for _ in range(N-1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def bfs(v):
    q = deque([v])

    visited = set()
    while q:
        front = q.popleft()
        for v in adj[front]:
            if v not in visited:
                q.append(v)
                visited.add(v)
                parent[v] = front

bfs(1)
for i in range(2, N+1):
    print(parent[i])
