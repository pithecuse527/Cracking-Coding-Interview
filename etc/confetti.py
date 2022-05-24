import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 0, 0, 0, 0, 0]
results = set()

def cover_uncover(sy, sx, paper, cover):
    global board
    for y in range(sy, sy+paper):
        for x in range(sx, sx+paper):
            if cover:
                board[y][x] = 0
            else:
                board[y][x] = 1

def cover_possible(sy, sx, paper):
    global board
    for y in range(sy, sy+paper):
        if y > 9:
            return False
        for x in range(sx, sx+paper):
            if x > 9 or board[y][x] == 0:
                return False
    return True

def dfs(cnt):
    global papers, results, board
    for y in range(10):
        for x in range(10):
            if board[y][x] == 1:
                for paper in [5,4,3,2,1]:
                    if papers[paper] < 5 and cover_possible(y, x, paper):
                        cover_uncover(y, x, paper, True)
                        papers[paper] += 1
                        results.add(dfs(cnt+1))
                        cover_uncover(y, x, paper, False)
                        papers[paper] -= 1
                if results:
                    return min(results)
                else:
                    return -1
    return cnt
  
results.add(dfs(0))
if -1 in results:
    results.remove(-1)
print(min(results) if results else -1)