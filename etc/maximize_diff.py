import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
perms = permutations(A, len(A))
max_val = 0

for perm in perms:
    val = 0
    for i in range(len(perm)-1):
        val += abs(perm[i]-perm[i+1])
    max_val = max(max_val, val)
print(max_val)
