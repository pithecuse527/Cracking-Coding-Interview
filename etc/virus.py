computers = int(input())
pairs = int(input())

adj = [list() for _ in range(computers+1)]
infected = set()    # regard this as a visited vertices set

def dfs(vertex):
    for adj_vertex in adj[vertex]:
        if adj_vertex not in infected:
            infected.add(adj_vertex)
            dfs(adj_vertex)

# computer vertex and edge ready
for _ in range(pairs):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

dfs(1)
print(len(infected)-1)  # do not count the origin (computer with number 1)
