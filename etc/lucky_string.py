from collections import Counter
import sys
input = sys.stdin.readline
S = input().strip()
counts = Counter(S)
answer = 0
def dfs(last_chr, picked):
    global answer
    if picked == len(S):
        answer += 1
        return
    
    for key in counts:
        if key == last_chr or counts[key] == 0:
            continue
        counts[key] -= 1
        dfs(key, picked+1)
        counts[key] += 1
dfs('', 0)
print(answer)