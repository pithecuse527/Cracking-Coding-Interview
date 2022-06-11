import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus = [(y, x) for x in range(N) for y in range(N) if lab[y][x] == 2]
answer = 1e9
to_visit = 0
for y in range(N):
    for x in range(N):
        if lab[y][x] == 0:
            to_visit += 1

def bfs(q):
    global answer
    dist = [[-1] * N for _ in range(N)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for y, x in q:
        dist[y][x] = 0
    max_dist = 0
    visit = 0
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if 0 <= ny < N and 0 <= nx < N and lab[ny][nx] != 1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[cy][cx]+1
                if lab[ny][nx] == 0:
                    max_dist = max(max_dist, dist[ny][nx])
                    visit += 1
                q.append((ny, nx))
    if visit == to_visit:
        answer = min(answer, max_dist)

virus_combi = combinations(virus, M)
for v in virus_combi:
    q = deque()
    for vy, vx in v:
        q.append((vy, vx))
    bfs(q)

if answer == 1e9:
    print(-1)
else:
    print(answer)
