N = int(input())

def dfs(accum, visited):
    if len(accum) >= N:
        if len(accum) == N:
            visited.add("".join(map(str, accum)))
        return
    
    for i in range(1, 5):
        dfs(accum+[i]*i, visited)
        # dfs(accum, visited)

visited = set()
dfs(list(), visited)
print(len(visited))