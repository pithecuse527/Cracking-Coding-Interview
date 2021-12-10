N, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp_sum = cards[i] + cards[j] + cards[k]
            if tmp_sum <= M and M - tmp_sum < M - answer:
                answer = tmp_sum
print(answer)