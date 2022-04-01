import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorder_idx = [0]*(N+1)

for i in range(N):
    inorder_idx[inorder[i]] = i

def divide(i_st, i_en, p_st, p_en):
    if p_st > p_en or i_st > i_en:
        return

    root = postorder[p_en]
    print(root, end=' ')
    
    left_tree_size = inorder_idx[root]-i_st
    right_tree_size = i_en-inorder_idx[root]
    divide(i_st, i_st+left_tree_size-1, p_st, p_st+left_tree_size-1)
    divide(i_en-right_tree_size+1, i_en, p_en-right_tree_size, p_en-1)

divide(0, N-1, 0, N-1)
print()