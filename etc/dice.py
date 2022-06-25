import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

def solution():
    min1, min2, min3 = 1e9, 1e9, 1e9
    for i in range(6):
        min1 = min(min1, nums[i])
        for j in range(i+1, 6):
            if i+j == 5:
                continue
            min2 = min(min2, nums[i]+nums[j])
            for k in range(j+1, 6):
                if j+k == 5 or i+k == 5:
                    continue
                min3 = min(min3, nums[i]+nums[j]+nums[k])
    return min1, min2, min3

if N == 1:
    print(sum(nums)-max(nums))
else:
    one_side, two_side, three_side = solution()
    answer = one_side*((N-2)**2+4*(N-2)*(N-1))+\
            two_side*((N-1)*4+(N-2)*4)+\
            4*three_side
    print(answer)
