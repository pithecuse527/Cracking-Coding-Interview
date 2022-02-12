from collections import Counter

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

answer = set()
def dfs(visited):
    if len(visited) == M:
        tmp = tuple([x[1] for x in visited])
        if tmp not in answer:
            answer.add(tmp)
        return
    
    for i in range(len(numbers)):
        if (i, numbers[i]) not in visited:
            visited.append((i, numbers[i]))
            dfs(visited)
            visited.pop()

dfs([])
for a in sorted(answer):
    print(" ".join(map(str, a)))