import heapq
num_ori = int(input())

# first version O(nlgn)
num = num_ori
heap = []
while num > 0:
    heapq.heappush(heap, num % 10)
    num //= 10

result = 0
mul = 1
while heap:
    result += heapq.heappop(heap) * mul
    mul *= 10
print(result)

# second version O(n)
bucket = [0 for _ in range(10)]
num = num_ori
while num:
    bucket[num % 10] += 1
    num //= 10

for i in range(9, -1, -1):
    while bucket[i] > 0:
        print(str(i), end='')
        bucket[i] -= 1
print()