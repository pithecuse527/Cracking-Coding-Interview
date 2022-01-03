n = int(input())
persons = []
answer = []

for i in range(n):
    t1, t2 = map(int, input().split())
    persons.append((t1, t2))

for i in range(n):
    cnt = 1
    for j in range(n):
        if persons[i][0] < persons[j][0] and persons[i][1] < persons[j][1]:
            cnt += 1
    answer.append(cnt)

for i in range(n):
    print(answer[i], end=' ')