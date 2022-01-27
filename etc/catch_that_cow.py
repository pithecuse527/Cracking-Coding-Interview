from collections import deque

MAX_VAL = 100000
N, K = map(int, input().split())

def bfs(start):
    q = deque([start])
    number_line = [0] * (MAX_VAL+1)
    
    while q:
        current = q.popleft()
        if current == K:
            return number_line[current]
        
        for c in [current-1, current+1, current*2]:
            if 0 <= c <= MAX_VAL and number_line[c] == 0:
                number_line[c] = number_line[current] + 1
                q.append(c)

print(bfs(N))
