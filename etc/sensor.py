import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
if K >= N:
    print(0)
    exit(0)
diffs = [sensors[i+1]-sensors[i] for i in range(N-1)]
diffs.sort()
for _ in range(K-1):
    diffs.pop()
print(sum(diffs))
