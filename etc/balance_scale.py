import sys
input = sys.stdin.readline
N = int(input())
weights = sorted(map(int, input().split()))

tmp = 1
for i in range(N):
    if weights[i] <= tmp:
        tmp += weights[i]
    else:
        break
print(tmp)
