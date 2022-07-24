from collections import deque
N, M, Q = map(int, input().split())
building = [deque(map(int, input().split())) for _ in range(N)]
cmds = [input().split() for _ in range(Q)]

def shift(y, d, building):
    if d == 0:
        building[y].appendleft(building[y].pop())
    else:
        building[y].append(building[y].popleft())

def duplicate(y1, y2, building):
    for i in range(M):
        if building[y1][i] == building[y2][i]:
            return True
    return False

def dfs(y, d1, d2, building):
    shift(y, d2, building)
    if 0 <= y+d1 < N and duplicate(y, y+d1, building):
        dfs(y+d1, d1, d2 ^ 1, building)

for i in range(Q):
    y, d = int(cmds[i][0])-1, cmds[i][1]
    if d == 'L':
        dfs(y, -1, 0, building)
        if y+1 < N and duplicate(y, y+1, building):
            dfs(y+1, 1, 1, building)
    else:
        dfs(y, -1, 1, building)
        if y+1 < N and duplicate(y, y+1, building):
            dfs(y+1, 1, 0, building)

for b in building:
    print(*b)
