import sys, copy
input = sys.stdin.readline
N, M = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
cctv_dirs = [[], [[0], [1], [2], [3]], [[1, 3], [0, 2]], [[0, 1], [1, 2], [2, 3], [3, 0]],
             [[0, 1, 3], [0, 1, 2], [1, 2, 3], [2, 3, 0]], [[0, 1, 2, 3]]]
dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cctvs = []
min_cnt = 1e9
for y in range(N):
    for x in range(M):
        if map_arr[y][x] not in [0, 6]:
            cctvs.append((y, x, map_arr[y][x]))

def get_cnt(map_arr):
    cnt = 0
    for y in range(N):
        for x in range(M):
            if map_arr[y][x] == 0:
                cnt += 1
    return cnt

def monitoring(y, x, watch_dirs, map_arr):
    for watch_dir in watch_dirs:
        ny, nx = y, x
        while True:
            ny, nx = ny+dydx[watch_dir][0], nx+dydx[watch_dir][1]
            if not (0 <= ny < N and 0 <= nx < M) or map_arr[ny][nx] == 6:
                break
            if map_arr[ny][nx] == 0:
                map_arr[ny][nx] = -1

def dfs(map_arr, cnt):
    global min_cnt

    if cnt == len(cctvs):
        min_cnt = min(min_cnt, get_cnt(map_arr))
        return
    
    y, x, cctv = cctvs[cnt]
    for watch_dirs in cctv_dirs[cctv]:
        next_map_arr = copy.deepcopy(map_arr)
        monitoring(y, x, watch_dirs, next_map_arr)
        dfs(next_map_arr, cnt+1)

dfs(map_arr, 0)
print(min_cnt)