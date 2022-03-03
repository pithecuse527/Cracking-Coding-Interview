from collections import deque
import sys, heapq
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

by, bx = -1, -1
for y in range(N):
    if (by, bx) != (-1, -1):
        break
    for x in range(N):
        if arr[y][x] == 9:
            arr[y][x] = 0
            by, bx = y, x

def bfs(y, x, baby_shark_size):
    fishes = []
    distance = [[0]*N for _ in range(N)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((y, x))

    while q:
        cy, cx = q.popleft()
        for dy, dx in direction:
            ny, nx = dy+cy, dx+cx
            if 0 <= ny < N and 0 <= nx < N and (ny, nx) and distance[ny][nx] == 0:
                if arr[ny][nx] <= baby_shark_size:
                    q.append((ny, nx))
                    distance[ny][nx] = distance[cy][cx]+1
                    if arr[ny][nx] < baby_shark_size and arr[ny][nx] != 0:
                        fishes.append((distance[ny][nx], ny, nx))
    if fishes:
        fishes.sort()
        return fishes[0]
    else:
        return None

eat = 0
moved = 0
baby_shark_size = 2
y, x = by, bx
while True:
    
    next_fish = bfs(y, x, baby_shark_size)
    if not next_fish:
        break
    dist, ny, nx = next_fish
    moved += dist
    arr[ny][nx] = 0
    arr[y][x] = 0
    y, x = ny, nx
    eat += 1

    if eat == baby_shark_size:
        eat = 0
        baby_shark_size += 1

print(moved)
