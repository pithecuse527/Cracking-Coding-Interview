import sys
input = sys.stdin.readline
N = int(input())
cows = [tuple(map(int, input().split())) for _ in range(N)]
cows.sort()

curr = 0
for arrive, interval in cows:
    if curr <= arrive:
        curr = arrive + interval
    else:
        curr += interval

print(curr)
    