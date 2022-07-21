from collections import deque
import sys
input = sys.stdin.readline

dirs = [(1, 0, 0), (-1, 0, 0),
        (0, -1, 0), (0, 1, 0), 
        (0, 0, -1), (0, 0, 1)]

def bfs(building, sl, sy, sx, el, ey, ex, L, R, C):
    q = deque()
    q.append((sl, sy, sx))
    visited = [[[-1]*C for y in range(R)] for l in range(L)]
    visited[sl][sy][sx] = 0
    while q:
        cl, cy, cx = q.popleft()
        for dl, dy, dx in dirs:
            nl, ny, nx = dl+cl, dy+cy, dx+cx
            if not (0 <= nl < L and 0 <= ny < R and
                    0 <= nx < C) or visited[nl][ny][nx] != -1 or\
                    building[nl][ny][nx] == '#':
                continue
            visited[nl][ny][nx] = visited[cl][cy][cx]+1
            q.append((nl, ny, nx))
    return visited[el][ey][ex]

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    building = [[]*R for _ in range(L)]
    for l in range(L):
        for y in range(R):
            building[l].append(input().rstrip())
        input()
    sl, sy, sx = -1, -1, -1
    el, ey, ex = -1, -1, -1
    for l in range(L):
        for y in range(R):
            for x in range(C):
                if building[l][y][x] == 'S':
                    sl, sy, sx = l, y, x
                if building[l][y][x] == 'E':
                    el, ey, ex = l, y, x
    t = bfs(building, sl, sy, sx, el, ey, ex, L, R, C)
    if t == -1:
        print('Trapped!')
    else:
        print('Escaped in %d minute(s).' % t)
