N = int(input())

chapters = []
for i in range(N):
    chapters.append(int(input()))
remaining_time = 30
answer = 0

for i in range(N):
    if remaining_time >= chapters[i]:
        remaining_time -= chapters[i]
        answer += 1
        if remaining_time == 0:
            remaining_time = 30
    else:
        if remaining_time >= chapters[i]/2:
            answer += 1
        remaining_time = 30
print(answer)
