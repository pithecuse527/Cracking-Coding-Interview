import heapq, sys
input = sys.stdin.readline
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = 1e9
problem_num = 0
def dijkstra(cave, n):
    q = [(cave[0][0], 0, 0)]
    distance = [[INF]*n for _ in range(n)]
    distance[0][0] = cave[0][0]

    while q:
        c_cost, cy, cx = heapq.heappop(q)
        if c_cost > distance[cy][cx]:
            continue
        for dy, dx in direction:
            ny = dy + cy
            nx = dx + cx
            if 0 <= ny < n and 0 <= nx < n:
                cost = c_cost + cave[ny][nx]
                if distance[ny][nx] > cost:
                    distance[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))
    return distance

while True:
    problem_num += 1
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    distance = dijkstra(cave, N)
    print('Problem {}: {}'.format(problem_num, distance[N-1][N-1]))
