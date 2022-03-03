import sys, heapq
from collections import deque
input = sys.stdin.readline
N = int(input())
space_arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(y, x, baby_shark):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((y, x))
    distance = [[0]*N for _ in range(N)]
    fishes = []

    while q:
        cy, cx = q.popleft()
        for dy, dx in direction:
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < N and 0 <= nx < N and distance[ny][nx] == 0 and baby_shark >= space_arr[ny][nx]:
                distance[ny][nx] = distance[cy][cx] + 1
                q.append((ny, nx))
                if baby_shark > space_arr[ny][nx] and space_arr[ny][nx] != 0:
                    heapq.heappush(fishes, (distance[ny][nx], ny, nx))
    if fishes:
        return heapq.heappop(fishes)
    else:
        return None

by, bx = -1, -1 
for y in range(N):
    if (by, bx) != (-1, -1):
        break
    for x in range(N):
        if space_arr[y][x] == 9:
            by, bx = y, x
            space_arr[y][x] = 0
baby_shark = 2
answer = 0
eat = 0
while True:
    space_arr[by][bx] = 0
    next_fish = bfs(by, bx, baby_shark)
    if not next_fish:
        break
    
    distance, ny, nx = next_fish
    answer += distance
    by, bx = ny, nx
    eat += 1
    if eat == baby_shark:
        baby_shark += 1
        eat = 0
print(answer)
