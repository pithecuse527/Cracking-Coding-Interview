import sys
input = sys.stdin.readline
N, M = map(int, input().split())
init_relation = [tuple(map(int, input().split())) for _ in range(M)]
height_relation = [[0]*N for _ in range(N)]

for x, y in init_relation:
    height_relation[x-1][y-1] = 1
    height_relation[y-1][x-1] = -1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or height_relation[i][j] in [1, -1]:
                continue
            if height_relation[i][k] == 1 and height_relation[k][j] == 1:
                height_relation[i][j] = 1
                height_relation[j][i] = height_relation[k][i] = height_relation[j][k] = -1
ans = 0
for row in height_relation:
    if row.count(0) == 1:
        ans += 1
print(ans)
