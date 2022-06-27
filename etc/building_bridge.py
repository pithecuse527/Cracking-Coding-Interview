from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 1e9

def numbering(sy, sx, num, visited):
    global board
    q = deque([(sy, sx)])
    visited[sy][sx] = True
    board[sy][sx] = num
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < N and 0 <= nx < N) or visited[ny][nx] or board[ny][nx] == 0:
                continue
            visited[ny][nx] = True
            q.append((ny, nx))
            board[ny][nx] = num

def building(num):
    global ans
    q = deque()
    dp = [[-1]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if board[y][x] == num:
                q.append((y, x))
                dp[y][x] = 0
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if board[ny][nx] != num and board[ny][nx] > 0:
                ans = min(ans, dp[cy][cx])
            if board[ny][nx] == 0 and dp[ny][nx] == -1:
                dp[ny][nx] = dp[cy][cx] + 1
                q.append((ny, nx))


num = 1
visited = [[False]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if not visited[y][x] and board[y][x] == 1:
            numbering(y, x, num, visited)
            num += 1

for i in range(1, num):
    building(i)
print(ans)
