from itertools import combinations
import sys
input = sys.stdin.readline

game_combi = list(combinations(range(6), 2))

def dfs(game_results, depth):
    global dfs_result

    if depth == 15:
        dfs_result = 1
        for result in game_results:
            if result.count(0) != 3:
                dfs_result = 0
                break
        return
    
    country1, country2 = game_combi[depth]
    for x, y in [(0, 2), (1, 1), (2, 0)]:
        if game_results[country1][x] > 0 and game_results[country2][y] > 0:
            game_results[country1][x] -= 1
            game_results[country2][y] -= 1
            dfs(game_results, depth+1)
            game_results[country1][x] += 1
            game_results[country2][y] += 1

ans = []
for _ in range(4):
    raw_total_result = list(map(int, input().split()))
    game_results = [raw_total_result[i:i+3] for i in range(0, 16, 3)]
    dfs_result = 0
    dfs(game_results, 0)
    ans.append(dfs_result)
    
print(*ans)