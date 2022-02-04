s = input()

stk = []

answer = 0
for c in s:
    if c == '(':
        stk.append(c)
    else:
        if stk:
            stk.pop()
        else:
            answer += 1
while stk:
    stk.pop()
    answer += 1
print(answer)
