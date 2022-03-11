import heapq, sys, copy
from itertools import combinations
input = sys.stdin.readline

N, M, D = map(int, input().split())
arr_ori = [list(map(int, input().split())) for _ in range(N)]

def enemies(arr):
    enemies_cnt = 0

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                enemies_cnt += 1

    return enemies_cnt

def move_enemy(arr):
    for y in range(-1, -N, -1):
        arr[y] = arr[y-1]
    arr[0] = [0 for _ in range(M)]
    
def neutralize_enemy(arr, archers):
    neutralized = set()
    neutralized_cnt = 0
    target_list = []
    
    for archer_x in archers:
        pq = []
        for y in range(N-1, -1, -1):
            for x in range(M):
                if arr[y][x] == 1:
                    diff = abs(N-y) + abs(archer_x-x)
                    if diff <= D:
                        heapq.heappush(pq, (diff, x, y))
        if pq:
            _, x, y = heapq.heappop(pq)
            target_list.append((y, x))
    
    for y, x in target_list:
        if (y, x) not in neutralized:
            neutralized.add((y, x))
            neutralized_cnt += 1
            arr[y][x] = 0

    return neutralized_cnt

def game(arr, archers):
    neutralized = 0
    while enemies(arr) != 0:
        neutralized += neutralize_enemy(arr, archers)
        move_enemy(arr)
    return neutralized

archers = list(combinations(range(M), 3))
max_val = 0
for a in archers:
    max_val = max(max_val, game(copy.deepcopy(arr_ori), a))
print(max_val)