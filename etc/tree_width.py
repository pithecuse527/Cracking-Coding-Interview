N = int(input())
tree = {}
traversed = []  # traversed result of inorder
lv_min_hash = dict()    # the left most loc. of level
lv_max_hash = dict()    # the right most loc. of level

class node:
    def __init__(self, val, left, right):
        self.left = left
        self.right = right
        self.val = val
        self.parent = -1

def inorder(n, lv):
    global traversed
    if tree[n].left != -1:
        inorder(tree[n].left, lv+1)
    
    traversed.append((n, lv))

    if tree[n].right != -1:
        inorder(tree[n].right, lv+1)

def find_max_width():
    cnt = 0     # traversed list runner
    height = 0  # tree height

    # find out the left most location and right most location of each level
    for t in traversed:  
        cnt += 1
        lv_min_hash[t[1]] = min(lv_min_hash.get(t[1], cnt), cnt)    # the left most loc.
        lv_max_hash[t[1]] = max(lv_max_hash.get(t[1], cnt), cnt)    # the right most loc.
        if height < t[1]:
            height = t[1]
    
    width = [0 for _ in range(height+1)]    # width of each level
    idx = 0
    w = 0
    for i in range(1, height+1):
        width[i] = lv_max_hash[i] - lv_min_hash[i] + 1
        if w < width[i]:
            w = width[i]
            idx = i
    return idx, w

# user input (node info.)
for _ in range(N):
    p, l, r = map(int, input().split())
    tree[p] = node(p, l, r)

# as there is no guarantee the number 1 is root,
# we need to figure out what the root is
for i in range(1, N+1):
    l = tree[i].left
    r = tree[i].right
    if l != -1:
        tree[l].parent = i
    if r != -1:
        tree[r].parent = i

root = -1
for i in range(1, N+1):
    if tree[i].parent == -1:
        root = i

inorder(root, 1)
idx, w = find_max_width()
print(idx, w)
