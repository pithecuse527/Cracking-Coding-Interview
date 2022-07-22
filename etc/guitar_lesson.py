import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lessons = list(map(int, input().split()))
left, right = max(lessons), sum(lessons)

ans = 1e9
while left <= right:
    mid = (left+right) // 2
    disk_cnt = 1
    disk_sum = 0
    for i in range(N):
        if disk_sum+lessons[i] <= mid:
            disk_sum += lessons[i]
        else:
            disk_sum = lessons[i]
            disk_cnt += 1
        if disk_cnt > M:
            break
    if disk_cnt > M:
        left = mid+1
    else:
        right = mid-1
        ans = min(ans, mid)
print(ans)
