import sys
input = sys.stdin.readline
N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingredients = [list()]
min_val = 1e9
ans_ingredients = []

def dfs(p, f, s, v, m, idx, contains):
    global min_val, ans_ingredients
    if m >= min_val:
        return

    if mp <= p and mf <= f and ms <= s and mv <= v:
        if m < min_val:
            min_val = m
            ans_ingredients = contains.copy()
        return
    if idx == N+1:
        return

    cp, cf, cs, cv, cm = ingredients[idx]
    contains.append(idx)    
    dfs(p+cp, f+cf, s+cs, v+cv, m+cm, idx+1, contains)
    contains.pop()
    dfs(p, f, s, v, m, idx+1, contains)
    return

for _ in range(N):
    ingredients.append(list(map(int, input().split())))
dfs(0, 0, 0, 0, 0, 1, list())
if min_val != 1e9:
    print(min_val)
    print(*ans_ingredients)
else:
    print(-1)
