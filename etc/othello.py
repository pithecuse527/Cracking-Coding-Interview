N = int(input())

board = [['.']*(8) for _ in range(8)]
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

board[3][3] = board[4][4] = 'W'
board[3][4] = board[4][3] = 'B'

color = ['B', 'W']
turn = 0

def update(d, y, x, c):
    stk = [(y+d[0], x+d[1])]

    # dfs
    while stk:
        top_y, top_x = stk[-1]
        if board[top_y][top_x] == '.':
            return
        if board[top_y][top_x] == c:
            stk.pop()
            if stk:
                next_y, next_x = stk[-1]
                board[next_y][next_x] = c
        else:
            stk.append((top_y+d[0], top_x+d[1]))

for _ in range(N):
    y, x = map(int, input().split())
    board[y][x] = color[turn]

    for i in range(8):
        update(direction[i], y, x, color[turn])
    
    turn = (turn + 1) % 2

whites = 0
blacks = 0
for i in range(1, 7):
    for j in range(1, 7):
        print(board[i][j], end='')
        if board[i][j] == 'B':
            blacks += 1
        if board[i][j] == 'W':
            whites += 1
    print()
winner = 'Black' if blacks > whites else 'White'
print(winner)