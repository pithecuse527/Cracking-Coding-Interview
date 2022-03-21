import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
N = int(input())
population = [0]+list(map(int, input().split()))
graph = [set()]
answer = 1e9
for _ in range(N):
    inpt = list(map(int, input().split()))[1:]
    graph.append(set(inpt))

def bfs(sector):
    start = sector[0]
    q = deque([start])
    sum_ = population[start]
    visited = set([start])

    while q:
        current = q.popleft()
        for adj in graph[current]:
            if adj not in visited and adj in sector:
                q.append(adj)
                visited.add(adj)
                sum_ += population[adj]
    return len(visited), sum_
    
for i in range(1, N//2+1):
    combis = combinations(range(1, N+1), i)
    for c in combis:
        c1 = list(c)
        c2 = list(set(range(1,N+1))-set(c1))
        v1, s1 = bfs(c1)
        v2, s2 = bfs(c2)
        if v1+v2 == N:
            answer = min(answer, abs(s1-s2))
if answer == 1e9:
    print(-1)
else:
    print(answer)