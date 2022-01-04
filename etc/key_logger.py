test_cases = int(input())

for _ in range(test_cases):
    s = input()

    stk1 = []
    stk2 = []
    for c in s:
        if c == '<':    # send the stk1 top to stk2
            if stk1:
                stk2.append(stk1.pop())
        elif c == '>':  # send the stk2 top to stk1
            if stk2:
                stk1.append(stk2.pop())
        elif c == '-':  # just pop from stk1
            if stk1:
                stk1.pop()
        else:   # normal char.
            stk1.append(c)

    # reamining stk2 elements
    while stk2:
        stk1.append(stk2.pop())
    print(''.join(stk1))
