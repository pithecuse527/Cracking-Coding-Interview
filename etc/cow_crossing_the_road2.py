from collections import deque
import sys
input = sys.stdin.readline
N, K, R = map(int, input().split())
not_avail = set()
farm = [[0]*(N+1) for _ in range(N+1)]

def bfs(sy, sx, cows):
    distance = [[-1]*(N+1) for _ in range(N+1)]
    distance[sy][sx] = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((sy, sx))
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (1 <= ny <= N and 1 <= nx <= N) or (cy, cx, ny, nx) in not_avail or distance[ny][nx] != -1:
                continue
            distance[ny][nx] = distance[cy][cx] + 1
            q.append((ny, nx))
    
    cnt = 0
    for y, x in cows:
        if distance[y][x] == -1:
            cnt += 1
    # print(cnt)
    return cnt

for _ in range(R):
    r, c, r_, c_ = map(int, input().split())
    not_avail.add((r, c, r_, c_))
    not_avail.add((r_, c_, r, c))

cows = []
for _ in range(K):
    y, x = map(int, input().split())
    farm[y][x] = 1
    cows.append((y, x))

cnt = 0
for y, x in cows:
    cnt += bfs(y, x, cows)
print(cnt//2)
