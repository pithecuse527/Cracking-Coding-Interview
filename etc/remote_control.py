import sys
N = int(input())
M = int(input())
input = sys.stdin.readline
not_avail = set(map(int, input().split()))

min_val = abs(N-100)
for c in range(1000001):
    for i in range(len(str(c))):
        if int(str(c)[i]) in not_avail:
            break
        elif len(str(c)) - 1 == i:
            min_val = min(min_val, abs(c-N)+len(str(c)))
print(min_val)
