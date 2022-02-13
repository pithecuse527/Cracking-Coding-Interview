N, M, R = map(int, input().split())

mtx = [list(map(int, input().split())) for _ in range(N)]

def rotate(mtx, start_y, start_x, end_y, end_x):
    # top row
    tmp1 = mtx[start_y][start_x]
    for i in range(start_x+1, end_x+1):
        mtx[start_y][i-1] = mtx[start_y][i]
    
    # left col
    tmp2 = mtx[end_y][start_x]
    for i in range(end_y-1, start_y, -1):
        mtx[i+1][start_x] = mtx[i][start_x]
    mtx[start_y+1][start_x] = tmp1

    # bottom row
    tmp3 = mtx[end_y][end_x]
    for i in range(end_x-1, start_x, -1):
        mtx[end_y][i+1] = mtx[end_y][i]
    mtx[end_y][start_x+1] = tmp2

    # right col
    for i in range(start_y+1, end_y):
        mtx[i-1][end_x] = mtx[i][end_x]
    mtx[end_y-1][end_x] = tmp3
print()
start_y, start_x, end_y, end_x = 0, 0, N-1, M-1
while start_y <= end_y and start_x <= end_x:
    tmp = ((end_y-start_y)*2 + (end_x-start_x)*2)
    rotate_cnt = R % tmp
    for i in range(rotate_cnt):
        rotate(mtx, start_y, start_x, end_y, end_x)
    start_y += 1
    start_x += 1
    end_y -= 1
    end_x -= 1

for m in mtx:
        print(" ".join(map(str, m)))