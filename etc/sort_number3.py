import sys

N = int(sys.stdin.readline())

bucket = [0 for x in range(10001)]

for _ in range(N):
    data = int(sys.stdin.readline())
    bucket[data] += 1

for i in range(1, 10001):
    while bucket[i] > 0:
        bucket[i] -= 1
        print(i)
