import heapq
N = int(input())
cards = []
total = 0

for i in range(N):
    heapq.heappush(cards, int(input()))

while(len(cards) != 1):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    sum_ = x+y
    heapq.heappush(cards, sum_)
    total += sum_
print(total)