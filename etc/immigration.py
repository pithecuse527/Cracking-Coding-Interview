from collections import deque
import sys
input = sys.stdin.readline
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def print_board():
    print()
    for r in board:
        print(r)
    print()

def immigration(unity):
    global board
    sums = 0
    for y, x in unity:
        sums += board[y][x]
    
    population = sums // len(unity)
    for y, x in unity:
        board[y][x] = population

def bfs(sy, sx, visit):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((sy, sx))
    unity = set()
    unity.add((sy, sx))
    visit[sy][sx] = True
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < N and 0 <= nx < N) or visit[ny][nx]:
                continue
            if L <= abs(board[cy][cx]-board[ny][nx]) <= R:
                unity.add((ny, nx))
                q.append((ny, nx))
                visit[ny][nx] = True
    immigration(unity)

    return True if len(unity) > 1 else False

cnt = 0
while True:
    flg = False
    visit = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visit[y][x]:
                if bfs(y, x, visit):
                    flg = True
    if not flg:
        break
    cnt += 1

print(cnt)   
