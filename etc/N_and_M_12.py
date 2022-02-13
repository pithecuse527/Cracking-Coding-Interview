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
    
    for i in range(N):
        tmp = (i, numbers[i])
        if not visited or tmp[1] >= visited[-1][1]:
            visited.append(tmp)
            dfs(visited)
            visited.pop()

dfs([])
for a in sorted(answer):
    print(" ".join(map(str, a)))