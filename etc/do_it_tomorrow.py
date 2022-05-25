import sys
input = sys.stdin.readline
N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]
tasks.sort(key=lambda x:x[1], reverse=True)

max_start = tasks[0][1]
for d, e in tasks:
    if max_start >= e:
        max_start = e - d
    else:
        max_start = max_start - d
print(max_start)
