N, M = map(int, input().split())

def dfs(visited):
    if len(visited) == M:
        for i in range(0,len(visited)):
            print(visited[i],end=" ")
        print()
        return
    
    for i in range(1, N+1):
        if not visited or (visited[-1] < i and i not in visited):
            visited.append(i)
            dfs(visited)
            visited.pop()
dfs([])
