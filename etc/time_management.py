import sys
input = sys.stdin.readline
N = int(input())
todo = [tuple(map(int, input().split())) for _ in range(N)]
todo.sort(key=lambda x:x[1], reverse=True)
start = todo[0][1]-todo[0][0]

for i in range(1, N):
    if start > todo[i][1]:
        start = todo[i][1] - todo[i][0]
    else:
        start -= todo[i][0]
if start < 0:
    print(-1)
else:
    print(start)
