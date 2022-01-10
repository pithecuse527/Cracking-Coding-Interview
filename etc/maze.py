from collections import deque

N, M = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# fence the maze with zeros
maze = [[0 for y in range(M+2)] for x in range(N+2)]

# visited cnt
cnt = [[0 for y in range(M+2)] for x in range(N+2)]

# visited node
visited = set()

def bfs(origin):
    visited = set()
    cnt[0][0] = 1
    q = deque([origin])
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (ny, nx) not in visited and maze[ny][nx] == 1:
                q.append((ny, nx))
                visited.add((ny, nx))
                cnt[ny][nx] = cnt[y][x] + 1

for i in range(1, N+1):
    row = input()
    for j in range(len(row)):
        maze[i][j+1] = int(row[j])

bfs((1,1))
print(cnt[N][M]+1)