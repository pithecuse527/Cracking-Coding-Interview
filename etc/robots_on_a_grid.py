from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
board = [input() for _ in range(N)]
dp = [[0]*N for _ in range(N)]

# case1: solvable with DP
dp_solvable = False
flag = False
for y in range(N):
    if not flag and board[y][0] == '#':
        flag = True
    dp[y][0] = 0 if flag else 1

flag = False
for x in range(N):
    if not flag and board[0][x] == '#':
        flag = True
    dp[0][x] = 0 if flag else 1

for y in range(1, N):
    for x in range(1, N):
        if board[y][x] == '#':
            dp[y][x] = 0
        else:
            dp[y][x] = (dp[y-1][x] + dp[y][x-1])%2147483647
if dp[-1][-1] > 0:
    dp_solvable = True
    print(dp[-1][-1])

# case2: solvable with BFS
if not dp_solvable:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((0, 0))
    visited = set()
    visited.add((0, 0))
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != '#' and (ny, nx) not in visited:
                q.append((ny, nx))
                visited.add((ny, nx))
    if (N-1, N-1) in visited:
        print('THE GAME IS A LIE')
    else:
        print('INCONCEIVABLE')