from collections import deque

N, M = map(int, input().split())
adj = [list() for _ in range(N+1)]
min_ = 1000000001
max_ = 0
result = 0

def bfs(origin, target, weight):
    q = deque([origin])
    visited = set()
    global result
    while q:
        v1 = q.popleft()
        for c in adj[v1]:
            if weight <= c[1] and c[0] not in visited:
                visited.add(c[0])
                if c[0] == target:
                    result = weight
                    return True
                q.append(c[0])
    return False

for _ in range(M):
    A, B, C = map(int, input().split())
    adj[A].append((B, C))
    adj[B].append((A, C))
    min_ = min(C, min_)
    max_ = max(C, max_)

origin, target = map(int, input().split())

while min_ <= max_:
    mid = (max_ + min_) // 2
    if bfs(origin, target, mid):
        min_ = mid+1
    else:
        max_ = mid-1
print(result)
