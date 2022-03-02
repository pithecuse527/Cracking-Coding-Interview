import sys, copy
from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken_distance = {}
store_loc = []
house_loc = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 2:
            store_loc.append((y, x))
        if arr[y][x] == 1:
            house_loc.append((y, x))

min_chicken_dis = 1e9
def get_chicken_dist(y, x, stores):
    min_dis = 1e9
    for sy, sx in stores:
        distance = abs(sy-y)+abs(sx-x)
        min_dis = min(min_dis, distance)
    return min_dis

def dfs(stores, pick):
    global min_chicken_dis
    
    if len(stores) == M:
        city_chicken_dist = 0
        for hy, hx in house_loc:
            city_chicken_dist += get_chicken_dist(hy, hx, stores)
        min_chicken_dis = min(min_chicken_dis, city_chicken_dist)
        return
    if pick >= len(store_loc):
        return
    dfs(stores+[store_loc[pick]], pick+1)
    dfs(stores, pick+1)
    

dfs([], 0)
print(min_chicken_dis)
