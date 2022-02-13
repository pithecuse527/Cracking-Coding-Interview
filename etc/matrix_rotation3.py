import sys, itertools, copy
input = sys.stdin.readline

N, M, K = map(int, input().split())
mtx = [[0]*M]
for _ in range(N):
    mtx.append([0]+list(map(int, input().split())))
rotate_query = [list(map(int, input().split())) for _ in range(K)]

def rotate(mtx, start_y, start_x, end_y, end_x):
     # top row
    tmp1 = mtx[start_y][end_x]
    for i in range(end_x-1, start_x-1, -1):
        mtx[start_y][i+1] = mtx[start_y][i]
    
    # right col
    tmp2 = mtx[end_y][end_x]
    for i in range(end_y-1, start_y, -1):
        mtx[i+1][end_x] = mtx[i][end_x]
    mtx[start_y+1][end_x] = tmp1

    # bottom row
    tmp3 = mtx[end_y][start_x]
    for i in range(start_x+1, end_x):
        mtx[end_y][i-1] = mtx[end_y][i]
    mtx[end_y][end_x-1] = tmp2

    # left col
    for i in range(start_y+1, end_y):
        mtx[i-1][start_x] = mtx[i][start_x]
    mtx[end_y-1][start_x] = tmp3

result = 1e9
for query in list(itertools.permutations(rotate_query, K)):
    mtx_copy = copy.deepcopy(mtx)
    for r, c, s in query:
        start_y = r-s
        start_x = c-s
        end_y = r+s
        end_x = c+s
        w = end_x-start_x+1
        h = end_y-start_y+1
        for i in range(min(w, h)//2):
            rotate(mtx_copy, start_y+i, start_x+i, end_y-i, end_x-i)

    for i in range(1, len(mtx_copy)):
        result = min(sum(mtx_copy[i]), result)
print(result)