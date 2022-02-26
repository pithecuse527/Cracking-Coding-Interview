N = int(input())
parent = list(map(int, input().split()))
to_del = int(input())
tree = {}
ans = 0
root = 0
for i in range(N):
    if parent[i] == -1:
        root = i
    else:
        tree[parent[i]] = tree.get(parent[i], list())+[i]

def dfs(parent):
    global ans
    if parent not in tree:
        ans += 1
        return
    
    for child in tree[parent]:
        if child == to_del:
            if len(tree[parent]) == 1:
                ans += 1
        else:
            dfs(child)

if to_del == root:
    print(0)
else:
    dfs(root)
    print(ans)
