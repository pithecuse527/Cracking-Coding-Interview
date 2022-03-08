import sys
input = sys.stdin.readline
N = int(input())
expr_ori = input()
max_val = -1e9

def dfs(idx, sub_total, expr):
    global max_val
    if idx >= len(expr)-2:
        max_val = max(max_val, sub_total)
        return
    
    sub_calc = eval(str(sub_total)+expr[idx]+expr[idx+1])
    dfs(idx+2, int(sub_calc), expr)
    
    if idx + 2 < len(expr)-1:
        sub_calc = eval(expr[idx+1]+expr[idx+2]+expr[idx+3])
        sub_calc = eval(str(sub_total)+expr[idx]+str(sub_calc))
        dfs(idx+4, int(sub_calc), expr)

if N == 1:
    print(expr_ori[0])
else:
    dfs(1, int(expr_ori[0]), expr_ori)
    print(max_val)