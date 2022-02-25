import sys, copy
input = sys.stdin.readline
N = int(input())    # the number of operators
INF = 1e9
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_value = -INF
min_value = INF
def backtracking(nums, ops, depth, calc_sum):
    global max_value, min_value
    if depth == N:  # exceed the max depth
        max_value = max(max_value, calc_sum)
        min_value = min(min_value, calc_sum)
    
    plus_cnt = ops[0]
    minus_cnt = ops[1]
    mul_cnt = ops[2]
    div_cnt = ops[3]

    if plus_cnt > 0:
        backtracking(nums, [plus_cnt-1, minus_cnt, mul_cnt, div_cnt], depth+1, calc_sum+nums[depth])
    if minus_cnt > 0:
        backtracking(nums, [plus_cnt, minus_cnt-1, mul_cnt, div_cnt], depth+1, calc_sum-nums[depth])
    if mul_cnt > 0:
        backtracking(nums, [plus_cnt, minus_cnt, mul_cnt-1, div_cnt], depth+1, calc_sum*nums[depth])
    if div_cnt > 0:
        backtracking(nums, [plus_cnt, minus_cnt, mul_cnt, div_cnt-1], depth+1, int(calc_sum/nums[depth]))
        

backtracking(numbers, operators, 1, numbers[0])
print(max_value)
print(min_value)
