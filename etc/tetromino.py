import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dirs = {0: (-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
max_val = -1
visited = [[False] * M for _ in range(N)]

def dfs(y, x, sub_sum, cnt, visited):
    global max_val
    if cnt == 4:
        max_val = max(max_val, sub_sum)
        return

    for d in range(4):
        ny, nx = y+dirs[d][0], x+dirs[d][1]
        if not (0 <= ny < N and 0 <= nx < M):
            continue

        if not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, sub_sum+arr[ny][nx], cnt+1, visited)
            visited[ny][nx] = False

def not_dfs(y, x):
    global max_val
    for i in range(4):  # ㅏ ㅓ ㅗ ㅜ 
        sum_ = arr[y][x]
        for j in range(3):
            looking = (i+j)%4
            ny, nx = y+dirs[looking][0], x+dirs[looking][1]
            if not (0 <= ny < N and 0 <= nx < M):
                break
            sum_ += arr[ny][nx]
        max_val = max(max_val, sum_)

for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(y, x, arr[y][x], 1, visited)
        visited[y][x] = False
        not_dfs(y, x)
print(max_val)