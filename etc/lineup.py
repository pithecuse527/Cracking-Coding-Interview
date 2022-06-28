import sys
input = sys.stdin.readline
T = int(input())

ans = 0
def dfs(ability, selected, accum, idx):
    global ans
    if idx == 11 and len(selected) == 11:
        ans = max(ans, accum)
        return
    
    for i in range(11):
        if ability[idx][i] == 0 or i in selected:
            continue
        selected.add(i)
        accum += ability[idx][i]
        dfs(ability, selected, accum, idx+1)
        selected.discard(i)
        accum -= ability[idx][i]

for _ in range(T):
    ans = 0
    ability = [list(map(int, input().split())) for _ in range(11)]
    dfs(ability, set(), 0, 0)
    print(ans)
