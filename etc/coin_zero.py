N, K = map(int, input().split())

answer = 0
coins = []
for i in range(N):
    coins.append(int(input()))

while K > 0:
    if coins[-1] <= K:
        K -= coins[-1]
        answer += 1
    else:
        coins.pop()

print(answer)