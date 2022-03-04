import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())
space_arr = [list(map(int, input().split())) for _ in range(R)]
new_spread = []
purifier = []
for y in range(R):
    if space_arr[y][0] == -1:
        purifier.append((y, 0))

def printing():
    for row in space_arr:
        print(row)

def spread(y, x):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    spread_amount = int(space_arr[y][x] / 5)
    for dy, dx in direction:
        ny, nx = y+dy, x+dx
        if 0 <= ny < R and 0 <= nx < C and space_arr[ny][nx] != -1:
            new_spread.append((ny, nx, spread_amount))
            space_arr[y][x] -= spread_amount

def purify1(sy, sx, ey, ex):
    # left col
    for y in range(ey-1, -1, -1):
        space_arr[y+1][sx] = space_arr[y][sx]
    
    # bottom row
    tmp1 = space_arr[ey][ex]
    for x in range(ex-1, sx, -1):
        space_arr[ey][x+1] = space_arr[ey][x]
    space_arr[ey][sx+1] = 0
    
    # right col
    tmp2 = space_arr[sy][ex]
    for y in range(sy+1, ey):
        space_arr[y-1][ex] = space_arr[y][ex]
    space_arr[ey-1][ex] = tmp1

    # upper row
    tmp3 = space_arr[sy][sx]
    for x in range(sx+1, ex):
        space_arr[sy][x-1] = space_arr[sy][x]
    space_arr[sy][ex-1] = tmp2
    space_arr[sy+1][sx] = tmp3

    space_arr[ey][sx] = -1   # purify

def purify2(sy, sx, ey, ex):
    # left col
    for y in range(sy+1, ey+1):
        space_arr[y-1][sx] = space_arr[y][sx]
    
    # upper row
    tmp1 = space_arr[sy][ex]
    for x in range(ex-1, sx, -1):
        space_arr[sy][x+1] = space_arr[sy][x]
    space_arr[sy][sx+1] = 0
    
    # right col
    tmp2 = space_arr[ey][ex]
    for y in range(ey-1, sy, -1):
        space_arr[y+1][ex] = space_arr[y][ex]
    space_arr[sy+1][ex] = tmp1

    # bottom row
    tmp3 = space_arr[ey][sx]
    for x in range(sx+1, ex):
        space_arr[ey][x-1] = space_arr[ey][x]
    space_arr[ey][ex-1] = tmp2
    space_arr[ey-1][sx] = tmp3

    space_arr[sy][sx] = -1   # purify

for t in range(T):
    spreading = []
    for y in range(R):
        for x in range(C):
            if space_arr[y][x] > 0:
                spreading.append((y, x))
    for sy, sx in spreading:
        spread(sy, sx)
    for ny, nx, amount in new_spread:
        space_arr[ny][nx] += amount
    new_spread = []    
    purify1(0, 0, purifier[0][0], C-1)
    purify2(purifier[1][0], purifier[1][1], R-1, C-1)

answer = 0
for y in range(R):
    for x in range(C):
        if space_arr[y][x] > 0:
            answer += space_arr[y][x]
print(answer)
