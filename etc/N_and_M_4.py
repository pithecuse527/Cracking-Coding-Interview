N, M = map(int, input().split())

def dfs(visited):
    if len(visited) == M:
        for v in visited:
            print(v, end=' ')
        print()
        return
    
    for i in range(1, N+1):
        if not visited or visited[-1] <= i:
            visited.append(i)
            dfs(visited)
            visited.pop()

dfs([])
