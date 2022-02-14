from collections import deque
import sys
input = sys.stdin.readline
V = int(input())    # the number of vertices

# graph ready
adj = [list() for _ in range(V+1)]
for _ in range(1, V+1):
    query = list(map(int, input().split()))
    v = query[0]
    for i in range(1, len(query)-1, 2):
        adj[v].append((query[i], query[i+1]))

# bfs
def get_distance(start):
    distance = [-1] * (V+1)
    distance[start] = 0
    q = deque([start])

    while q:
        front = q.popleft()
        for c, w in adj[front]:
            if distance[c] == -1:
                distance[c] = distance[front]+w
                q.append(c)

    return distance

distance = get_distance(1)

farthest = 0
farthest_dist = 0
for i in range(1, len(distance)):
    if distance[i] > farthest_dist:
        farthest = i
        farthest_dist = distance[i]

distance = get_distance(farthest)
print(max(distance))
