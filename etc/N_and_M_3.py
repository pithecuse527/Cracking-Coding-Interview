N, M = map(int, input().split())

def dfs(visited):
    if len(visited) == M:
        for i in range(len(visited)):
            print(visited[i],end=" ")
        print()
        return
    
    for i in range(1, N+1):
        visited.append(i)
        dfs(visited)
        visited.pop()
dfs([])
