N = int(input())

conference = [tuple(map(int, input().split())) for _ in range(N)]
conference.sort(key=lambda x:(x[1], x[0]))

end = 0
cnt = 0
for c in conference:
    if c[0] >= end:
        end = c[1]
        cnt += 1
print(cnt)