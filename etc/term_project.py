import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
T = int(input())
team_matched = []

def dfs(team, curr, selection, visited):
    global team_matched
    visited.add(curr)
    team.append(curr)
    next_ = selection[curr]

    if next_ in visited:
        if next_ in team:
            team_matched += team[team.index(next_):]
        return
    else:
        dfs(team, next_, selection, visited)
        
for _ in range(T):
    N = int(input())
    selection = [0]+list(map(int, input().split()))
    visited = set()
    team_matched = []
    for i in range(1, N+1):
        if i not in visited:
            dfs(list(), i, selection, visited)
    
    print(N-len(team_matched))