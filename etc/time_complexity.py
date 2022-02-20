C = int(input())

answer = 0
for _ in range(C):
    code = input()
    for_cnt = code.count('for')
    while_cnt = code.count('while')
    answer = max(answer, for_cnt+while_cnt)
print(answer)