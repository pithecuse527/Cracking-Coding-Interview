import sys
input = sys.stdin.readline
N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))
dirs = {1:(0, 1), 2:(0, -1), 3:(-1, 0), 4:(1, 0)}
def roll(d, dice):
    if d == 1:
        tmp = dice[6]
        dice[6] = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[4]
        dice[4] = tmp
    elif d == 2:
        tmp = dice[6]
        dice[6] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[3]
        dice[3] = tmp
    elif d == 3:
        tmp = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = tmp
    else:
        tmp = dice[6]
        dice[6] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[2]
        dice[2] = tmp

def located(board, dice, y, x):
    if board[y][x] == 0:
        board[y][x] = dice[6]
    else:
        dice[6] = board[y][x]
        board[y][x] = 0

dice = [0]*7  # dummy for dice[0]
located(board, dice, y, x)
for c in cmd:
    ny, nx = dirs[c][0]+y, dirs[c][1]+x
    if 0 <= ny < N and 0 <= nx < M:
        y, x = ny, nx
        roll(c, dice)
        located(board, dice, y, x)
        print(dice[1])