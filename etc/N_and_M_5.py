N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(visited):
    if len(visited) == M:
        for v in visited:
            print(v, end=' ')
        print()
        return
    
    for i in numbers:
        if i not in visited:
            visited.append(i)
            dfs(visited)
            visited.pop()

dfs([])
