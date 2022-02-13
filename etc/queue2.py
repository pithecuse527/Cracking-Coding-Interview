from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    query_input = input().split()
    query = query_input[0]
    value = None
    if len(query_input) > 1:
        query = query_input[0]
        value = query_input[1]
    
    if query == 'push':
        q.append(value)
    elif query == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif query == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif query == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif query == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif query == 'size':
        print(len(q))



