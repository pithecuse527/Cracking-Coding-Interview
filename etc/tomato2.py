from collections import deque
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dirs = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]

def bfs(boxes):
    q = deque()

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if boxes[z][y][x] == 1:
                    q.append((z, y, x))

    while q:
        cz, cy, cx = q.popleft()
        for dz, dy, dx in dirs:
            nz, ny, nx = dz+cz, dy+cy, dx+cx
            if not (0 <= nz < H and 0 <= ny < N and 0 <= nx < M):
                continue
            if boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = boxes[cz][cy][cx] + 1
                q.append((nz, ny, nx))

bfs(boxes)
ans = 1
for z in range(H):
    for y in range(N):
        for x in range(M):
            if boxes[z][y][x] == 0:
                print(-1)
                exit()
            ans = max(ans, boxes[z][y][x])
print(ans-1)
