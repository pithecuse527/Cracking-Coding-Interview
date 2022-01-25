N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

color_match = {'W': 0, 'B': 1}
colors = ['W', 'B']

def counting(board, row_st, col_st):
    color_idx = color_match[board[row_st][col_st]]
    cnt1 = 0
    for i in range(row_st, row_st+8, 1):
        for j in range(col_st, col_st+7, 2):
            if board[i][j] != colors[color_idx]:
                cnt1 += 1
            if board[i][j+1] == colors[color_idx]:
                cnt1 += 1
        color_idx = (color_idx + 1) % 2

    return min(cnt1, 64-cnt1)

row_st = 0
min_cnt = 65
while row_st <= N-8:
    col_st = 0
    while col_st <= M-8:
        cnt = counting(board, row_st, col_st)
        if cnt < min_cnt:
            min_cnt = cnt
        col_st += 1 
    row_st += 1
print(min_cnt)
