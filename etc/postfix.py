infix = input()
stk = []
postfix = []
priorities = {'+':1, '-':1, '*':2, '/':2}

for c in infix:
    if 'A' <= c <= 'Z':
        postfix.append(c)
    else:
        if not stk:
            stk.append(c)
        elif c == ')':
            while stk[-1] != '(':
                postfix.append(stk.pop())
            stk.pop()
        elif c == '(':
            stk.append(c)
        else:
            while stk and stk[-1] != '(' and priorities[stk[-1]] >= priorities[c]:
                postfix.append(stk.pop())
            stk.append(c)
while stk:
    postfix.append(stk.pop())
for c in postfix:
    print(c, end='')
print()