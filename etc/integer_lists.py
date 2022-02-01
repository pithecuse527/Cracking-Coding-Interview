from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    int_arr = input().strip()[1:-1].split(",")

    if n != 0:
        q = deque(int_arr)
    else:
        q = deque()

    error_flg = False
    r = 0
    for command in p:
        if command == 'R':
            r = (r+1)%2
        else:
            if q:
                if r == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                print('error')
                error_flg = True
                break
    
    if not error_flg:
        if r == 0:
           print('['+','.join(q)+']')
        else:
            q.reverse()
            print('['+','.join(q)+']')
