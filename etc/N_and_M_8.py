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
        if not visited or (visited[-1] <= i):
            visited.append(i)
            dfs(visited)
            visited.pop()

dfs([])
