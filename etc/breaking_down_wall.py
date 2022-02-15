from collections import deque
import sys
input = sys.stdin.readline

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
array = []
for _ in range(N):
    row = list(str(input().rstrip()))
    array.append(list(map(int, row)))

def bfs():
    q = deque()
    q.append((0, 0, 0))
    distance = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    distance[0][0][0] = 1

    while q:
        cy, cx, w = q.popleft()
        
        if cy == N-1 and cx == M-1:
            return distance[cy][cx][w]
        
        for dy, dx in direction:
            ny = dy + cy
            nx = dx + cx
            if 0 <= ny < N and 0 <= nx < M:
                if array[ny][nx] == 0 and distance[ny][nx][w] == 0:
                    distance[ny][nx][w] = distance[cy][cx][w]+1
                    q.append((ny, nx, w))
                if array[ny][nx] == 1 and w == 0:
                    distance[ny][nx][w+1] = distance[cy][cx][w]+1
                    q.append((ny, nx, w+1))
    return -1
print(bfs())