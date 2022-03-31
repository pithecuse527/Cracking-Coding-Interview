import sys
from collections import deque
F, S, G, U, D = map(int, input().split())

it_takes = [1e9]*(F+1)
def bfs():
    q = deque([S])
    it_takes[S] = 0
    while q:
        curr = q.popleft()
        if U+curr <= F and it_takes[curr]+1 < it_takes[U+curr]:
            it_takes[U+curr] = it_takes[curr]+1
            q.append(U+curr)
        if -D+curr > 0 and it_takes[curr]+1 < it_takes[-D+curr]:
            it_takes[-D+curr] = it_takes[curr]+1
            q.append(-D+curr)
bfs()
if it_takes[G] != 1e9:
    print(it_takes[G])
else:
    print('use the stairs')
