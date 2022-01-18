N = int(input())

bricks = [(0,0,0,0)]
for i in range(1, N+1):
    area, height, weight = map(int, input().split())
    bricks.append((i, area, height, weight))

bricks.sort(key=lambda x:x[3])

dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        if bricks[i][1] > bricks[j][1]:
            dp[i] = max(dp[i], dp[j]+bricks[i][2])

max_val = max(dp)
i = N
result = []

while i > 0:
    if max_val == dp[i]:
        result.append(bricks[i][0])
        max_val -= bricks[i][2]
    i -= 1

print(len(result))
result.reverse()
for x in result:
    print(x)