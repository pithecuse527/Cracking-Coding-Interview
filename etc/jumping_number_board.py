import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(5)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answers = set()

def dfs(cy, cx, collected):
    if len(collected) == 6:
        collected_tuple = tuple(collected)
        answers.add(collected_tuple)
        return
    
    for dy, dx in dirs:
        ny, nx = dy+cy, dx+cx
        if not (0 <= ny < 5 and 0 <= nx < 5):
            continue
        collected.append(board[ny][nx])
        if tuple(collected) not in answers:
            dfs(ny, nx, collected)
        collected.pop()

for y in range(5):
    for x in range(5):
        collected = [board[y][x]]
        dfs(y, x, collected)
print(len(answers))