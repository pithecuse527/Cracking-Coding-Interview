import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]

ans_time = 1e9
ans_height = 1e9
for target in range(257):
    inventory_add = 0
    inventory_sub = 0
    for y in range(N):
        for x in range(M):
            if heights[y][x] >= target:
                inventory_add += heights[y][x] - target
            else:
                inventory_sub += target - heights[y][x]
    if inventory_add + B >= inventory_sub and ans_time >= inventory_add*2+inventory_sub:
        ans_time = inventory_add*2+inventory_sub
        ans_height = target
print(ans_time, ans_height)
