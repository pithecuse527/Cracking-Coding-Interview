import sys
sys.setrecursionlimit(10**6)

T = int(input())
directions = [(-1, 0), (1, 0), (0,-1), (0,1)]

def dfs(y, x, visited, arr):
    cnt = 1
    visited.add((y, x))

    for d in directions:
        next_y, next_x = y+d[0], x+d[1]
        if arr[next_y][next_x] != 0 and (next_y, next_x) not in visited:
            visited.add((next_y, next_x))
            cnt += dfs(next_y, next_x, visited, arr)
    return cnt

for _ in range(T):
    visited = set()
    answer = 0
    M, N, K = map(int, input().split())
    arr = [[0] * (M+2) for _ in range(N+2)]

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y+1][x+1] = 1

    for y in range(1, N+1):
        for x in range(1, M+1):
            cnt = 0
            if arr[y][x] == 1 and (y, x) not in visited:
                cnt += dfs(y, x ,visited, arr)
            if cnt > 0:
                answer += 1
                
    print(answer)
