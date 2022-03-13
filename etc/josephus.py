from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

q = deque([i for i in range(1, N+1)])
ans = []

while q:
    for _ in range(K):
        q.append(q.popleft())
    ans.append(q.pop())

print('<', end='')
for i in range(len(ans)-1):
    print('{}, '.format(ans[i]), end='')
print('{}>'.format(ans[-1]))