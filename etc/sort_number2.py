import sys

N = int(sys.stdin.readline())

lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()
for i in lst:
    print(i)
    