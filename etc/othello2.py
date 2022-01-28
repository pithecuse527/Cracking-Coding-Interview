T = int(input())



for test_case in range(1, T + 1):
    color = ['.', 'B', 'W']
    board = None
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

    N, M = map(int, input().split())
    direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    board = [['.']*(N+2) for _ in range(N+2)]
    
    # init. the first setting
    init_pvt = N // 2
    board[init_pvt][init_pvt] = board[init_pvt+1][init_pvt+1] = 'W'
    board[init_pvt][init_pvt+1] = board[init_pvt+1][init_pvt] = 'B'

    for _ in range(M):
        y, x, c = map(int, input().split())
        board[y][x] = color[c]

        for i in range(8):
            update(direction[i], y, x, color[c])

    whites = 0
    blacks = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 'B':
                blacks += 1
            if board[i][j] == 'W':
                whites += 1

    print('#{0} {1} {2}'.format(test_case, blacks, whites))
