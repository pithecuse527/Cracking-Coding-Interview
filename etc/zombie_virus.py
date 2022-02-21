from collections import deque
import sys
input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
completed = [[False]*M for _ in range(N)]

def printing():
    print()
    for r in arr:
        print(r)

def spread(q):
    next_q = deque()

    while q:
        cy, cx = q.popleft()
        if arr[cy][cx] == 3 or arr[cy][cx] == -1:
            continue
        for dy, dx in directions:
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = arr[cy][cx]
                    next_q.append((ny, nx))
                elif arr[cy][cx] != arr[ny][nx] and arr[ny][nx] != -1 and not completed[ny][nx]:
                    arr[ny][nx] = 3
    for y, x in next_q:
        completed[y][x] = True

    return next_q

def bfs(q):
    while q:
        q = spread(q)

q = deque()
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1 or arr[y][x] == 2:
            q.append((y,x))
            completed[y][x] = True
bfs(q)
cnt1 = 0
cnt2 = 0
cnt3 = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            cnt1 += 1
        elif arr[y][x] == 2:
            cnt2 += 1
        elif arr[y][x] == 3:
            cnt3 += 1
print(cnt1,cnt2,cnt3)

# printing()
