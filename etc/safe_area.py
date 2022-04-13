import sys
input = sys.stdin.readline
N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 위, 아래, 왼, 오른 방향

def dfs(pvt_height, y, x, visited):
    visited.add((y, x))
    stk = [(y, x)]
    
    while stk:  # 스택이 빌 때까지
        cy, cx = stk.pop()  # 다음으로 방문할 위치 pop (깊이 우선이므로 top이 곧 깊은 위치)
        for dy, dx in dirs:
            ny = dy + cy  # 다음 방문 위치
            nx = dx + cx
            if not (0 <= ny < N and 0 <= nx < N):  # 범위 체크
                continue
            
            # dfs를 하면서 방문한 적이 없고 pvt_height보다 높은 위치라면 다음으로 방문하도록...
            if (ny, nx) not in visited and heights[ny][nx] > pvt_height:
                stk.append((ny, nx))   # 다음 방문 위치 쌓기
                visited.add((ny, nx))  # 방문 기록 저장

# 높이가 가장 큰 지역의 높이 구하기
# (주어진 배열에서 최대값을 찾으면 되는 것입니다)
max_height = max(list(map(max, heights)))  

ans = 0  # 최종 답안(안전 영역의 최대 개수)

# 안전 영역의 범위는 0 ~ max_height(높이가 가장 큰 지역의 높이)
for pvt_height in range(max_height):
    visited = set()  # 방문 기록
    safe_area = 0    # 현재 pvt_height 기준으로 안전 영역이 몇 개?

    # 2D 배열을 모두 돌면서...
    for y in range(N):
        for x in range(N):
            # 만약 pvt_height 보다 높은 지점이고 DFS를 통해 방문한 적이 없다면 DFS시작
            if heights[y][x] > pvt_height and (y, x) not in visited:
                safe_area += 1
                dfs(pvt_height, y, x, visited)
    ans = max(ans, safe_area)  # 최종 답안 업데이트
print(ans)