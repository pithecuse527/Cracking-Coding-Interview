import sys
S = input()
stk = []

bracket_opened = False
for ch in S:
    if ch == '>':
        bracket_opened = False
        print(ch, end='')  
    elif bracket_opened:
        print(ch, end='')
    elif ch == '<':
        while stk:
            print(stk.pop(), end='')
        bracket_opened = True
        print(ch, end='')
    elif ch == ' ':
        while stk:
            print(stk.pop(), end='')
        print(' ', end='')
    else:
        stk.append(ch)
while stk:
    print(stk.pop(), end='')
print()
