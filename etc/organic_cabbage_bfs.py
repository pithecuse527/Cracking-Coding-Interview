from collections import deque
T = int(input())
direction = [(1,0), (-1,0), (0, 1), (0, -1)]

def bfs(init_y, init_x, farm, visited):
    if (init_y, init_x) in visited:
        return 0
    q = deque()
    q.append((init_y, init_x))
    visited.add((init_y, init_x))

    cnt = 1
    while q:
        curr_y, curr_x = q.popleft()
        for d in direction:
            next_y, next_x = curr_y+d[0], curr_x+d[1]
            if farm[next_y][next_x] != 0 and (next_y, next_x) not in visited:
                visited.add((next_y, next_x))
                q.append((next_y, next_x))
                cnt += 1
    return cnt
    
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*(M+2) for _ in range(N+2)]
    
    for i in range(K):
        x, y = map(int, input().split())
        farm[y+1][x+1] = 1

    visited = set()
    answer = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if farm[i][j] == 1 and bfs(i, j, farm, visited) > 0:
                answer += 1
    print(answer)
