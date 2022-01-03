N, M = map(int, input().split())

def dfs(visited):
    if len(visited) == M:
        for i in range(0,len(visited)):
            print(visited[i],end=" ")
        return
    
    for i in range(1, N+1):
        if i not in visited:
            visited.append(i)
            dfs(visited)
            visited.pop()
dfs([])