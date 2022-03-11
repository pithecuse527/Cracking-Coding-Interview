import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d_ = map(int, input().split())
stat_arr = [list(map(int, input().split())) for _ in range(N)]

def printing():
    print()
    for r in stat_arr:
        print(r)
    

def dfs(y, x, to, cnt):
    d = {0: (-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
    stat_arr[y][x] = 2
    # printing()
    to_next = to
    while True:
        to_next = (to_next-1)%4
        ny, nx = y+d[to_next][0], x+d[to_next][1]
        if stat_arr[ny][nx] == 0:
            break
        if to_next == to:
            # print('stuck')
            ny, nx = y+d[(to_next+2)%4][0], x+d[(to_next+2)%4][1]
            break
    if stat_arr[ny][nx] == 1:
        return cnt
    
    if stat_arr[ny][nx] == 0:
        cnt += 1
        
    return dfs(ny, nx, to_next, cnt)

print(dfs(r, c, d_, 1))
