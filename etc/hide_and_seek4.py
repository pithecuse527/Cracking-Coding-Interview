from collections import deque
N, K = map(int, input().split())

def bfs(start):
    q = deque([start])
    visited = dict()
    visited[start] = 0
    visited_from = dict()
    visited_from[start] = 0
    
    while q:
        curr = q.popleft()
        if curr == K:
            print(visited[K])
            stk = [K]
            while curr != N:
                curr = visited_from[curr]
                stk.append(curr)
            
            while stk:
                print(stk.pop(), end=' ')
            print()
            return
            
        if curr-1 >= 0 and curr-1 not in visited:
            visited[curr-1] = visited[curr]+1
            visited_from[curr-1] = curr
            q.append(curr-1)
            
        if curr*2 <= 1e5 and curr*2 not in visited:
            visited[curr*2] = visited[curr]+1
            visited_from[curr*2] = curr
            q.appendleft(curr*2)
            
        if curr+1 <= 1e5 and curr+1 not in visited:
            visited[curr+1] = visited[curr]+1
            visited_from[curr+1] = curr
            q.append(curr+1)

bfs(N)
