import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ds = [tuple(map(int, input().split())) for _ in range(M)]
dirs = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def move_cloud(A, d, s, clouds):
    watered_loc = set()
    for _ in range(s):
        for cy, cx in clouds:
            ny, nx = (cy+dirs[d][0])%N, (cx+dirs[d][1])%N
            cy, cx = ny, nx
    
    for cy, cx in clouds:
        ny, nx = (cy+s*dirs[d][0])%N, (cx+s*dirs[d][1])%N
        watered_loc.add((ny, nx))
    
    for y, x in watered_loc:
        A[y][x] += 1

    return watered_loc

def copy_water(A, watered_loc):
    dydx = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for cy, cx in watered_loc:
        for dy, dx in dydx:
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < N and 0 <= nx < N and A[ny][nx] > 0:
                A[cy][cx] += 1

def clouding(A, watered_loc):
    clouds = set()
    for y in range(N):
        for x in range(N):
            if (y, x) in watered_loc or A[y][x] < 2:
                continue
            A[y][x] -= 2
            clouds.add((y, x))
    return clouds

def printing(A):
    print()
    for y in range(N):
        for x in range(N):
            print(A[y][x], end=' ')
        print()

clouds = set([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])
for d, s in ds:
    watered_loc = move_cloud(A, d, s, clouds)
    copy_water(A, watered_loc)
    clouds = clouding(A, watered_loc)

answer = 0
for y in range(N):
    answer += sum(A[y])
print(answer)