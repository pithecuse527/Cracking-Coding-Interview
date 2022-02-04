import heapq

N, K = map(int, input().split())
q = list(map(int, input().split()))
heapq.heapify(q)

lst = []
while K > 0:
    lst.append(heapq.heappop(q))
    K -= 1
print(lst[-1])
