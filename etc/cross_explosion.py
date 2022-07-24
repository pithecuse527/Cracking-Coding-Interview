from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())
dirs = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}

# 중력에 의한 정리
def cleanup(board): 
    new_board = [[0]*N for _ in range(N)]
    for x in range(N):
        y_runner = N-1
        for y in range(N-1, -1, -1):
            if board[y][x] != 0:
                new_board[y_runner][x] = board[y][x]
                y_runner -= 1

    return new_board

# 재귀...
def remove_spread(y, x, d, cnt, board):
    if not (0 <= y < N and 0 <= x < N) or cnt == 0:
        return
    board[y][x] = 0
    remove_spread(y+dirs[d][0], x+dirs[d][1], d, cnt-1, board)

def cross_remove(y, x, cnt, board):

    # current pivot
    board[y][x] = 0

    # up
    remove_spread(y+dirs[0][0], x+dirs[0][1], 0, cnt-1, board)

    # right
    remove_spread(y+dirs[1][0], x+dirs[1][1], 1, cnt-1, board)

    # down
    remove_spread(y+dirs[2][0], x+dirs[2][1], 2, cnt-1, board)

    # left
    remove_spread(y+dirs[3][0], x+dirs[3][1], 3, cnt-1, board)

cross_remove(R-1, C-1, board[R-1][C-1], board)
new_board = cleanup(board)

for b in new_board:
    print(*b)