import sys
input = sys.stdin.readline
N, K = map(int, input().split())

visited = set()
def dfs(accum, collected):
    global visited
    if accum == N:
        collected_tuple = tuple(collected)
        if collected_tuple not in visited:
            visited.add(collected_tuple)
        return
    
    for n in [1,2,3]:
        if accum + n > N:  # pruning
            continue
        collected.append(n)
        dfs(accum+n, collected)
        collected.pop()

dfs(0, list())
if len(visited) < K:
    print(-1)
    exit(0)
ans = sorted(visited)[K-1]
ans_str = ""
for a in ans:
    ans_str += str(a)+'+'
print(ans_str[:-1])
