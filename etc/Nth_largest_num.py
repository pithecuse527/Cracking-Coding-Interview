import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = []
for i in range(N):
    for j in range(N):
        heapq.heappush(q, arr[i][j])
        if len(q) > N:
            heapq.heappop(q)
print(heapq.heappop(q))
