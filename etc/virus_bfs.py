from collections import deque

V = int(input())
E = int(input())
adj = [set() for _ in range(V+1)]

def bfs(v):
    q = deque([v])
    visited = set([v])
    cnt = 0
    while q:
        curr = q.popleft()
        for c in adj[curr]:
            if c not in visited:
                visited.add(c)
                q.append(c)
                cnt += 1
    return cnt

for _ in range(E):
    x, y = map(int, input().split())
    adj[x].add(y)
    adj[y].add(x)
print(bfs(1))
