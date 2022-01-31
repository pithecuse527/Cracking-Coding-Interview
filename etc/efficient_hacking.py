import sys
input=sys.stdin.readline

N, M = map(int, input().split())
arr = [list() for _ in range(N+1)]
answers = []
max_cnt = 0

for _ in range(M):
    A, B = map(int, input().split())
    arr[B].append(A)

for i in range(1, N+1):
    cnt = 0
    stk = [i]
    visited = [False] * (N+1)
    visited[i] = True

    while stk:
        top = stk.pop()
        cnt += 1
        for c in arr[top]:
            if not visited[c]:
                visited[c] = True
                stk.append(c)

    if cnt > max_cnt:
        answers = [i]
        max_cnt = cnt
    elif cnt == max_cnt:
        answers.append(i)

for a in answers:
    print(a, end=' ')
print()
