import copy
dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))
answer = None   # answer dwarfs array

def promising(partial_dwarfs): 
    if len(partial_dwarfs) > 7 or sum(partial_dwarfs) > 100:
        return False
    return True

def dfs(visited, partial_dwarfs, idx): # backtracking
    global answer
    if answer:  # base case1
        return

    # base case2
    if len(partial_dwarfs) == 7 and sum(partial_dwarfs) == 100:
        answer = copy.deepcopy(partial_dwarfs)
        return
    
    for i in range(idx, 9):
        if i not in visited:    # not to visit the visited node(dwarf)
            partial_dwarfs.append(dwarfs[i])
            visited.add(i)
            if promising(partial_dwarfs):  # feasibility check (pruning)
                dfs(visited, partial_dwarfs, idx+1)
            visited.remove(i)
            partial_dwarfs.pop()

dfs(set(), [], 0)
answer.sort()
for a in answer:
    print(a)
