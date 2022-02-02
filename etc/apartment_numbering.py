from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(input())
arr = ['0'*(N+2)]
for _ in range(N):
    row = '0' + input() + '0'
    arr.append(row)
arr.append('0'*(N+2))

visited = set()
def bfs(y, x):
    if (y, x) in visited:
        return 0
    visited.add((y, x))

    q = deque([(y, x)])
    
    cnt = 0
    while q:
        y_curr, x_curr = q.popleft()
        cnt += 1
        for y_add, x_add in direction:
            y_next = y_curr + y_add
            x_next = x_curr + x_add
            if (y_next, x_next) not in visited and arr[y_next][x_next] == '1':
                visited.add((y_next, x_next))
                q.append((y_next, x_next))
    return cnt

answer = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == '1':
            cnt = bfs(i, j)
            if cnt > 0:
                answer.append(cnt)
print(len(answer))
answer.sort()
for a in answer:
    print(a)
