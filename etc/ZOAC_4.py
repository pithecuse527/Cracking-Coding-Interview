H, W, N, M = map(int, input().split())

cnt = 0
for i in range(0, H, N+1):
    for j in range(0, W, M+1):
        cnt += 1
print(cnt)
