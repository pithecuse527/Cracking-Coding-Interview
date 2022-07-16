import sys
input = sys.stdin.readline
N = int(input())
requests = list(map(int, input().split()))
M = int(input())

low, high = 0, max(requests)
while low <= high:
    limit = (low+high) // 2
    accum = 0
    for request in requests:
        if request <= limit:
            accum += request
        else:
            accum += limit
    if accum <= M:
        low = limit+1
    else:
        high = limit-1
print(high)
