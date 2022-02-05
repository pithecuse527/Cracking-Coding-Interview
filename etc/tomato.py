from collections import deque

M, N = map(int, input().split())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            q.append((y, x))

def bfs():
    while q:
        y, x = q.popleft()
        for d in direction:
            ny, nx = y+d[0], x+d[1]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x] + 1
                q.append((ny, nx))
bfs()
answer = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            print(-1)
            exit()
        answer = max(answer, arr[y][x])
print(answer - 1)