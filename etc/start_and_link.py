import sys
input = sys.stdin.readline
N = int(input())
INF = 1e9
mtx = [list(map(int, input().split())) for _ in range(N)]
people = set([x for x in range(N)])
min_diff = INF

def scoring(team, team_size):
    score = 0
    for i in range(team_size-1):
        for j in range(i+1, team_size):
            score += mtx[team[i]][team[j]]
            score += mtx[team[j]][team[i]]
    return score

def dfs(start_team, team_size, pvt):
    global min_diff
    if team_size == N // 2:
        start_team_score = scoring(list(start_team), team_size)
        link_team = people.difference(start_team)
        link_team_score = scoring(list(link_team), team_size)
        min_diff = min(min_diff, abs(start_team_score-link_team_score))
        return
    
    for i in range(pvt, N):
        start_team.append(i)
        dfs(start_team, team_size+1, i+1)
        start_team.pop()
    
dfs([], 0, 0)
print(min_diff)