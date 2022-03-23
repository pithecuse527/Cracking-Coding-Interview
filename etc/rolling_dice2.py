import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0]*(M+1)]
for _ in range(N):
    board.append([0]+list(map(int, input().split())))
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
moving = 1
dice = [0, 1, 2, 3, 4, 5, 6]

def roll(d, dice):
    if d == 0:
        tmp = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = tmp
    elif d == 1:
        tmp = dice[6]
        dice[6] = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[4]
        dice[4] = tmp
    elif d == 2:
        tmp = dice[6]
        dice[6] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[2]
        dice[2] = tmp
    else:
        tmp = dice[6]
        dice[6] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[3]
        dice[3] = tmp

def dfs(y, x, num, visited):
    partial_score = board[y][x]
    for dy, dx in dirs:
        ny, nx = dy+y, dx+x
        if 0 <= ny <= N and 0 <= nx <= M and (ny, nx) not in visited and board[ny][nx] == num:
            visited.add((ny, nx))
            partial_score += dfs(ny, nx, num, visited)
    return partial_score
        
y, x = 1, 1
score = 0
d = 1
for i in range(K):
    ny, nx = dirs[d][0]+y, dirs[d][1]+x
    if not (1 <= ny <= N and 1 <= nx <= M):
        d = (d+2)%4
        ny, nx = dirs[d][0]+y, dirs[d][1]+x
    roll(d, dice)
    visited = set()
    visited.add((ny, nx))
    score += dfs(ny, nx, board[ny][nx], visited)
    if dice[6] > board[ny][nx]:
        d = (d+1)%4
    if dice[6] < board[ny][nx]:
        d = (d-1)%4
    y, x = ny, nx
print(score)