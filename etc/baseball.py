from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

def game(turns):
    i = 0
    score = 0
    for inning in innings:
        outs = 0
        b1, b2, b3 = 0, 0, 0
        while outs < 3:
            result = inning[turns[i]]
            if result == 0:
                outs += 1
            elif result == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif result == 2:
                score += (b2+b3)
                b1, b2, b3 = 0, 1, b1
            elif result == 3:
                score += (b1+b2+b3)
                b1, b2, b3 = 0, 0, 1
            else:
                score += (b1+b2+b3+1)
                b1, b2, b3 = 0, 0, 0
            i = (i+1)%9
    return score

max_score = 0
for perm in permutations(range(1, 9), 8):
    turns = list(perm[:3])+[0]+list(perm[3:])
    max_score = max(max_score, game(turns))
print(max_score)