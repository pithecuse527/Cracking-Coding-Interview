from collections import deque
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
graph = [list() for _ in range(N+1)]

def usado_videos(start, k, graph):
    q = deque([start])
    distance = [1e9]*(N+1)

    visited = set([start])
    while q:
        front = q.popleft()
        for next_, cost in graph[front]:
            if next_ not in visited:
                visited.add(next_)
                q.append(next_)
                distance[next_] = min(distance[front], cost)
    
    # print(distance) 
    cnt = 0
    for dist in distance:
        if dist >= k and dist != 1e9:
            cnt += 1
    return cnt

for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, node = map(int, input().split())
    print(usado_videos(node, k, graph))
