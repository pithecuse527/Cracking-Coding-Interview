import sys
input = sys.stdin.readline
N = int(input())
marbles = list(map(int, input().split()))

answer = 0
def dfs(accum, selected):
    global answer
    if len(selected) == N-2:
        answer = max(answer, accum)
        return
    
    for i in range(1, N-1):
        if i in selected:
            continue
        selected.add(i)
        runner1, runner2 = i-1, i+1
        while runner1 in selected:
            runner1 -= 1
        while runner2 in selected:
            runner2 += 1
        accum += marbles[runner1]*marbles[runner2]
        dfs(accum, selected)
        selected.discard(i)
        accum -= marbles[runner1]*marbles[runner2]

dfs(0, set())
print(answer)