import sys
input = sys.stdin.readline
N = 10001
numbers = set([x for x in range(1, N)])
not_self_nums = set()

for x in range(1, N):
    num_sum = x
    while x > 0:
        num_sum += (x%10)
        x //= 10
    not_self_nums.add(num_sum)

for x in sorted(numbers-not_self_nums):
    print(x)