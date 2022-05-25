from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

def bfs(sy, sx, ty, tx, store_locs):
    q = deque()
    q.append((sy, sx))
    visited = set()
    while q:
        y, x  = q.popleft()
        if abs(y-ty)+abs(x-tx) <= 1000:
            return "happy"
        for store_y, store_x in store_locs:
            if (store_y, store_x) in visited:
                continue
            if abs(store_y-y)+abs(store_x-x) <= 1000:
                visited.add((store_y, store_x))
                q.append((store_y, store_x))
    return "sad"

for _ in range(T):
    N = int(input())
    hy, hx = map(int, input().split())
    store_locs = [tuple(map(int, input().split())) for _ in range(N)]
    ty, tx = map(int, input().split())
    print(bfs(hy, hx, ty, tx, store_locs))

