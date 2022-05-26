from gc import collect
import sys
input = sys.stdin.readline

def print_nums(collection):
    for num in sorted(collection):
        print(num, end=' ')
    print()

def promising(collection, S, idx):
    if len(collection) + len(S[idx+1:]) < 6:
        return False
    return True

def dfs(collection, S, idx):
    
    if len(collection) == 6:
        print_nums(collection)
        return
    if idx >= len(S):
        return
    
    collection.add(S[idx])
    if promising(collection, S, idx):
        dfs(collection, S, idx+1)
    collection.discard(S[idx])
    dfs(collection, S, idx+1)

while True:
    usr_inpt = list(map(int, input().split()))
    if usr_inpt[0] == 0:
        break
    K, S = usr_inpt[0], usr_inpt[1:]
    dfs(set(), S, 0)
    print()
