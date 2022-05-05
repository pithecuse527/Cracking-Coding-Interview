from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(arr, y, x, visited):
    q = deque()
    q.append((y, x))
    visited.add((y, x))
    decrease = []
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < N and 0 <= nx < M):
                continue
            if arr[ny][nx] == 0:
                decrease.append((cy, cx))
            elif (ny, nx) not in visited:
                visited.add((ny, nx))
                q.append((ny, nx))
    if len(decrease) == 0:
        return False

    for dy, dx in decrease:
        arr[dy][dx] = max(arr[dy][dx]-1, 0)
    return True

year = 0
while True:
    cnt = 0
    visited = set()
    year += 1

    for y in range(N):
        for x in range(M):
            if arr[y][x] != 0 and (y, x) not in visited:
                bfs(arr, y, x, visited)
                cnt += 1

    if cnt > 1:
        print(year-1)
        break
    
    if cnt == 0:
        print(0)
        break
