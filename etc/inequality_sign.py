from select import select
import sys
input = sys.stdin.readline
K = int(input())
inequalities = list(input().split())

def check(e, n1, n2):
    if e == '<':
        if n1 < n2:
            return True
        return False
    else:
        if n1 > n2:
            return True
        return False

def dfs(selected, nums, idx, candidates):
    if idx == K+1:
        candidates.add("".join(map(str, nums)))
        return

    for i in range(10):
        if i in selected:
            continue

        if idx == 0:
            nums.append(i)
            selected.add(i)
            dfs(selected, nums, idx+1, candidates)
            nums.pop()
            selected.discard(i)    
        else:
            if check(inequalities[idx-1], nums[-1], i):
                nums.append(i)
                selected.add(i)
                dfs(selected, nums, idx+1, candidates)
                nums.pop()
                selected.discard(i)
            
candidates = set()
dfs(set(), list(), 0, candidates)
print(max(candidates))
print(min(candidates))
