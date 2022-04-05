import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = 1e9
curr_ans = 0
r1, r2 = 0, 0

while True:
    if curr_ans >= M:
        ans = min(ans, r2-r1)
        curr_ans -= lst[r1]
        r1 += 1
    elif r2 == N:
        break
    else:
        curr_ans += lst[r2]
        r2 += 1
if ans == 1e9:
    ans = 0
print(ans)

