from collections import deque
N, K = map(int, input().split())

def bfs(start):
    q = deque([start])
    visited = dict()  # key := location, val := visited time
    visited[start] = 1
    cnt = 0

    while q:
        curr = q.popleft()
        if curr == K:
            return visited[K]-1
        
        if curr-1 >= 0 and curr-1 not in visited:
            q.append(curr-1)
            visited[curr-1] = visited[curr]+1
        
        if curr*2 <= 1e5 and curr*2 not in visited:
            q.appendleft(curr*2)
            visited[curr*2] = visited[curr]

        if curr+1 <= 1e5 and curr+1 not in visited:
            q.append(curr+1)
            visited[curr+1] = visited[curr]+1

print(bfs(N))
