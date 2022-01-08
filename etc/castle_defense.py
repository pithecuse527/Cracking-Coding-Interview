N, M = map(int, input().split())

castle = []
for _ in range(N):
    row = input()
    castle.append(row)

# row search
row_need = 0
for i in range(N):
    guard = False
    for j in range(M):
        if castle[i][j] == 'X':
            guard = True
            break
    if not guard:
        row_need += 1

col_need = 0
for i in range(M):
    guard = False
    for j in range(N):
        if castle[j][i] == 'X':
            guard = True
            break
    if not guard:
        col_need += 1
print(max(row_need, col_need))
