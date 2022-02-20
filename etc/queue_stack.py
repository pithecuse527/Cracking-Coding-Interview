from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))


qs = [] # queuestack

# queuestack init.
for i in range(N):
    if A[i] == 1:   # stk
        qs.append([B[i]])
    else:
        qs.append(deque([B[i]]))

itm = None
for i in range(M):
    itm = C[i]
    for j in range(N):
        if A[j] == 1:
            continue
        qs[j].append(itm)
        itm = qs[j].popleft()
    print(itm, end=' ')
print()