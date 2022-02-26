import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    arr.append((int(input()), i))
arr_sorted = sorted(arr)

idx_diff = [arr[i][1]-arr_sorted[i][1] for i in range(N)]
print(-(min(idx_diff)-1))
