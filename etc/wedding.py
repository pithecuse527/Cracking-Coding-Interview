from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
relation = {}
for _ in range(M):
    a, b = map(int, input().split())
    relation[a] = relation.get(a, list())+[b]
    relation[b] = relation.get(b, list())+[a]

def bfs():
    q = deque()
    q.append((1, 0))
    visited = set([1])
    cnt = 0

    while q:
        p, dist = q.popleft()
        if p not in relation or dist >= 2:
            continue
        for np in relation[p]:
            if np not in visited:
                visited.add(np)
                q.append((np, dist+1))
                cnt += 1
    return cnt
print(bfs())