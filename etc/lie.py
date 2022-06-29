import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tmp = list(map(int, input().split()))
knows = 0
knows_lst = set()
if len(tmp) > 0:
    knows_lst = set(tmp[1:])
root = [x for x in range(N+1)]

def find(child):
    global root
    if root[child] != child:
        root[child] = find(root[child])
    return root[child]
    

def union(child1, child2):
    global root
    child1_root = find(child1)
    child2_root = find(child2)
    
    if child1_root in knows_lst and child2_root in knows_lst:
        return

    if child1_root in knows_lst:
        root[child2_root] = child1_root
    elif child2_root in knows_lst:
        root[child1_root] = child2_root
    else:
        if child1_root < child2_root:
            root[child2_root] = child1_root
        else:
            root[child1_root] = child2_root

parties = []
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    for i in range(len(party)-1):
        union(party[i], party[i+1])
    parties.append(party)

ans = 0
for party in parties:
    for i in range(len(party)):
        if find(party[i]) in knows_lst:
            break
    else:
        ans += 1
print(ans)
