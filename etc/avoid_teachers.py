import sys
input = sys.stdin.readline
N = int(input())
board = [input().split() for _ in range(N)]
teachers = []
result = False
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for y in range(N):
    for x in range(N):
        if board[y][x] == 'T':
            teachers.append((y, x))

def student_detacted(board):
    for ty, tx in teachers:
        for dy, dx in dirs:
            y, x = ty, tx
            while 0 <= y < N and 0 <= x < N:
                if board[y][x] == 'S':
                    return True
                if board[y][x] == 'O':
                    break
                y += dy
                x += dx
    return False

def dfs(cnt, board):
    global result
    if cnt > 3:
        return
    if cnt == 3:
        if not student_detacted(board):
            result = True

    if result:
        return
    
    for y in range(N):
        for x in range(N):
            if board[y][x] == 'X':
                board[y][x] = 'O'
                dfs(cnt+1, board)
                if result:
                    return
                board[y][x] = 'X'

dfs(0, board)
print("YES" if result else "NO")
