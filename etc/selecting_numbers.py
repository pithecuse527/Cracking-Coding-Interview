import sys
input = sys.stdin.readline
N, M = map(int, input().split())
array = [int(input().rstrip()) for _ in range(N)]
array.sort()
left, right = 0, 1

answer = sys.maxsize
while left < N and right < N:
    if array[right]-array[left] == M:
        print(M)
        exit(0)
    if array[right]-array[left] < M:
        right += 1
        continue
    answer = min(answer, array[right]-array[left])
    left += 1
print(answer)