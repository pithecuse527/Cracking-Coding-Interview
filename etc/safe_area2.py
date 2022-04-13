from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(pvt_height, y, x, visited):
    q = deque()
    q.append((y, x))
    visited.add((y, x))
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny = dy + cy
            nx = dx + cx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if (ny, nx) not in visited and heights[ny][nx] > pvt_height:
                q.append((ny,nx))
                visited.add((ny,nx))
max_height = max(list(map(max, heights)))  

ans = 0  # 최종 답안(안전 영역의 최대 개수)

# 안전 영역의 범위는 0 ~ max_height(높이가 가장 큰 지역의 높이)
for pvt_height in range(max_height):
    visited = set()
    safe_area = 0    # 현재 pvt_height 기준으로 안전 영역이 몇 개?

    # 2D 배열을 모두 돌면서...
    for y in range(N):
        for x in range(N):
            # 만약 pvt_height 보다 높은 지점이고 DFS를 통해 방문한 적이 없다면 DFS시작
            if heights[y][x] > pvt_height and (y, x) not in visited:
                safe_area += 1
                bfs(pvt_height, y, x, visited)
    ans = max(ans, safe_area)  # 최종 답안 업데이트
print(ans)