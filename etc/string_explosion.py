import sys
input = sys.stdin.readline
S = input()[:-1]
bomb = input()[:-1]
stk = []

for c in S:
    stk.append(c)
    cnt = 0
    while cnt != len(bomb) and len(stk) >= len(bomb) and stk[-1-cnt] == bomb[-1-cnt]:
        cnt += 1
    
    if cnt == len(bomb):
        for i in range(cnt):
            stk.pop()
if stk:
    print(''.join(stk))
else:
    print('FRULA')