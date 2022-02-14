import sys
input = sys.stdin.readline
N = int(input())

adj_mtx = [list() for _ in range(N+1)]
for _ in range(N-1):
    p, c, w = map(int, input().split())
    adj_mtx[p].append((c, w))
    adj_mtx[c].append((p, w))

def dfs(start, weight, visited):
    stk = [start]
    distances = [0] * (N+1)
    distances[start] = weight

    while stk:
        top = stk.pop()
        visited[top] = True
        for c, w in adj_mtx[top]:
            if not visited[c]:
                stk.append(c)
                distances[c] = distances[top]+w
    return max(distances)

def find_diameter(root):
    distances = []
    
    for c, w in adj_mtx[root]:
        visited = [False] * (N+1)
        visited[root] = True
        distances.append(dfs(c, w, visited))
    return sorted(distances)

answer = 0
for i in range(1, N+1):
    distances = find_diameter(i)
    if len(distances) > 1:
        answer = max(answer, distances[-1]+distances[-2])
print(answer)
