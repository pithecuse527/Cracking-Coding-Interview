import sys
input = sys.stdin.readline
N, M, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 0

def dfs(y, x, home_loc, milks, hp, cnt):
    global max_cnt, board
    for my, mx in milks:
        if board[my][mx] == 2:
            curr_dist = abs(y-my)+abs(x-mx)
            if curr_dist <= hp:
                board[my][mx] = 0
                dfs(my, mx, home_loc, milks, hp+H-curr_dist, cnt+1)
                board[my][mx] = 2

    if abs(y-home_loc[0])+abs(x-home_loc[1]) <= hp:
        max_cnt = max(max_cnt, cnt)

def find_home_milk():
    home_loc = (-1, -1)
    milks = []
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                home_loc = (y, x)
            elif board[y][x] == 2:
                milks.append((y, x))
    return home_loc, milks

home_loc, milks = find_home_milk()
dfs(home_loc[0], home_loc[1], home_loc, milks, M, 0)
print(max_cnt)