from os import stat
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pools = sorted([list(map(int, input().split())) for _ in range(N)])
cnt = 0

for i in range(len(pools)):
    start, end = pools[i]
    pane_num = 0
    if (end-start) % L == 0:
        pane_num = (end-start)//L
    else:
        pane_num = (end-start)//L+1
    
    cnt += pane_num
    if i+1 < N:
        curr_end = start+pane_num*L
        next_start = pools[i+1][0]
        if next_start < curr_end:
            pools[i+1][0] = curr_end
print(cnt)
