from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))
partial_sum = 0
partial_sum_dict = {0:1}

cnt = 0
for num in A:
    partial_sum += num
    if partial_sum - K in partial_sum_dict:
        cnt += partial_sum_dict[partial_sum-K]
    partial_sum_dict[partial_sum] = partial_sum_dict.get(partial_sum, 0) + 1
print(cnt)
