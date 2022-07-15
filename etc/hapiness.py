import sys
input = sys.stdin.readline
N = int(input())
max_val, min_val = 0, 1e9
nums = map(int, input().split())
for num in nums:
    max_val = max(max_val, num)
    min_val = min(min_val, num)
print(max_val-min_val)
