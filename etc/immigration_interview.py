import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

left, right = 0, max(times)*M
result = -1

while left <= right:
    mid = (left+right) // 2
    passed = 0
    for time in times:
        passed += mid // time
        if passed > M:
            break
    if passed >= M:
        right = mid - 1
        result = mid
    else:
        left = mid + 1
print(result)
