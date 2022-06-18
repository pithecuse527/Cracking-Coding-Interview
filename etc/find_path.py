import sys
input = sys.stdin.readline
N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if mtx[i][j] == 1 or (mtx[i][k] == 1 and mtx[k][j] == 1):
                mtx[i][j] = 1

for row in mtx:
    print(*row)
