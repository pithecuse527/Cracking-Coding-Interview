from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
img = [list(input()) for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(color, y, x, visited):
    q = deque([(y, x)])
    visited[y][x] = True
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in direction:
            ny = dy + cy
            nx = dx + cx
            if 0 <= ny < N and 0 <= nx < N and img[ny][nx] == color and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True

normal_cnt = 0
visited = [[False]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            normal_cnt += 1
            bfs(img[y][x], y, x, visited)
print(normal_cnt)

blind_cnt = 0
visited = [[False]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if img[y][x] == 'G':
            img[y][x] = 'R'

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            blind_cnt += 1
            bfs(img[y][x], y, x, visited)
print(blind_cnt)
