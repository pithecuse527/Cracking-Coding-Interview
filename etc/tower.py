N = int(input())
towers = [0]+list(map(int, input().split()))
stk = [(towers[1], 1)]
answer = [0]

for i in range(2, N+1):
    while stk:
        if stk[-1][0] < towers[i]:
            stk.pop()
            if not stk:
                answer.append(0)
        else:
            answer.append(stk[-1][1])
            break
    stk.append((towers[i], i))
for a in answer:
    print(a, end=' ')
print()
