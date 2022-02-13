import sys
input=sys.stdin.readline

A, B = map(int, input().split())

def dfs(depth, numb):
    if numb > B:
        return False
    
    if numb == B:
        print(depth)
        return True
    
    if not dfs(depth+1, numb*2):
        return dfs(depth+1, int(str(numb)+'1'))
    else:
        return True

if not dfs(1, A):
    print(-1)