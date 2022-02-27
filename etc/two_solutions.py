import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = N-1
left_ans = left
right_ans = right
optimal_sum = 2e9+2

while left < right:
    tmp_sum = arr[left]+arr[right]
    if abs(tmp_sum) < optimal_sum:
        optimal_sum = abs(tmp_sum)
        left_ans = left
        right_ans = right

    if tmp_sum < 0:
        left += 1
    elif tmp_sum == 0:
        break
    else:
        right -= 1

print(arr[left_ans], arr[right_ans])
