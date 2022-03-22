import sys
input = sys.stdin.readline
gears = [list()]+[list(input())[:-1] for _ in range(4)]
K = int(input())
cmds = [list(map(int, input().split())) for _ in range(K)]

def rotate(gear, clockwise):
    if clockwise == 1:
        tmp = gear[-1]
        for i in range(6, -1, -1):
            gear[i+1] = gear[i]
        gear[0] = tmp
    else:
        tmp = gear[0]
        for i in range(1, 8):
            gear[i-1] = gear[i]
        gear[-1] = tmp

def dfs(gear, clockwise, visited):
    visited.add(gear)
    next_clockwise = -1 if clockwise == 1 else 1
    if gear == 1:
        if gear+1 not in visited and gears[gear][2] != gears[gear+1][6]:
            dfs(gear+1, next_clockwise, visited)
    elif gear == 2 or gear == 3:
        if gear-1 not in visited and gears[gear][6] != gears[gear-1][2]:
            dfs(gear-1, next_clockwise, visited)
        if gear+1 not in visited and gears[gear][2] != gears[gear+1][6]:
            dfs(gear+1, next_clockwise, visited)
    else:
        if gear-1 not in visited and gears[gear][6] != gears[gear-1][2]:
            dfs(gear-1, next_clockwise, visited)
    rotate(gears[gear], clockwise)

for cmd in cmds:
    dfs(cmd[0], cmd[1], set())

answer = 0
for i in range(1, 5):
    if gears[i][0] == '1':
        answer += 2**(i-1)
print(answer)