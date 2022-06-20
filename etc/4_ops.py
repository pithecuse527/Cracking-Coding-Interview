from collections import deque
import sys
input = sys.stdin.readline
S, T = map(int, input().split())

def bfs():
    ops = ['*', '+', '/']
    q = deque()
    q.append((S, ''))
    visited = set()
    visited.add(S)

    while q:
        curr_num, curr_op = q.popleft()
        if curr_num == T:
            return curr_op
        
        for op in ops:
            next_num = int(eval(str(curr_num)+op+str(curr_num)))
            if 0 <= next_num <= T and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, curr_op+op))
    return -1

if S == T:
    print(0)
else:
    print(bfs())