from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1
L = int(input())
cmds = {}
for _ in range(L):
    X, C = input().split()
    cmds[int(X)] = C
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

d = 1
snake = deque([(0, 0)])
cnt = 0
while True:
    cnt += 1
    hy, hx = snake[-1][0], snake[-1][1]  # snake head
    ny, nx = hy+dirs[d][0], hx+dirs[d][1]
    if cnt in cmds:
        if cmds[cnt] == 'L':
            d = (d-1)%4
        else:
            d = (d+1)%4
    if not (0 <= ny < N and 0 <= nx < N) or (ny, nx) in snake:
        break
    if board[ny][nx] == 0:
        snake.popleft()
    if board[ny][nx] == 1:
        board[ny][nx] = 0
    snake.append((ny, nx))
print(cnt)