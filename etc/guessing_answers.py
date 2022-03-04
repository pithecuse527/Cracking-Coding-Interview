N, M = map(int, input().split())
answers = [0]+list(map(int, input().split()))+[0]
corrects = [0]+list(map(int, input().split()))
corrects.sort()
j = 1
for i in range(1, N+1):
    if j < M+1 and i == corrects[j]:
        j += 1
        continue

    while True:
        answers[i] = (answers[i]+1)%5+1
        if answers[i] != answers[i-1] and answers[i] != answers[i+1]:
            break

for i in range(1, N+1):
    print(answers[i], end=' ')
print()