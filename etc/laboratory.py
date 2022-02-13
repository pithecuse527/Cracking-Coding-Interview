from collections import deque
import copy, sys
input = sys.stdin.readline
N, M = map(int, input().split())

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
lab_array_ori = [[-1]*(M+2)]
answer = -1

for _ in range(N):
    row = [-1]+list(map(int, input().split()))+[-1]
    lab_array_ori.append(row)
lab_array_ori.append([-1]*(M+2))

def walling_and_bfs(cnt, walled_lab_arr):
    if cnt == 3:
        bfs(walled_lab_arr)
        return
    
    # walling dfs
    for y in range(1, N+1):
        for x in range(1, M+1):
            if walled_lab_arr[y][x] == 0:
                walled_lab_arr[y][x] = 1
                walling_and_bfs(cnt+1, walled_lab_arr)
                walled_lab_arr[y][x] = 0

def bfs(walled_lab_arr):
    global answer
    lab_array = copy.deepcopy(walled_lab_arr)
    
    # queue ready
    q = deque()
    for y in range(1, N+1):
        for x in range(1, M+1):
            if lab_array[y][x] == 2:
                q.append((y, x))

    # bfs implement
    while q:
        curr_y, curr_x = q.popleft()
        for d_y, d_x in direction:
            next_y = curr_y + d_y
            next_x = curr_x + d_x
            if lab_array[next_y][next_x] == -1:
                continue

            if lab_array[next_y][next_x] == 0:
                lab_array[next_y][next_x] = 2
                q.append((next_y, next_x))
    
    # counting the result
    cnt = 0
    for y in range(1, N+1):
        for x in range(1, M+1):
            if lab_array[y][x] == 0:
                cnt += 1
    answer = max(answer, cnt)

walling_and_bfs(0, lab_array_ori)

print(answer)
