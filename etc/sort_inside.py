import heapq

num = int(input())
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
