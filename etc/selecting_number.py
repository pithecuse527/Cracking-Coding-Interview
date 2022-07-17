from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]
directed_graph = defaultdict(list)
for i in range(1, N+1):
    directed_graph[numbers[i-1]].append(i)

answer = set()
def dfs(u, stk, visited):
    global answer
    for v in directed_graph[u]:
        if v in visited:
            while stk:
                top = stk.pop()
                answer.add(top)
                if top == v:
                    break
            return
        visited.add(v)
        # stk.append(v)
        dfs(v, stk+[v], visited)
        visited.discard(v)
for i in range(1, N+1):
    dfs(i, list(), set())
answer = sorted(answer)
print(len(answer), *answer, sep='\n')
