import heapq
from collections import deque
import sys
input = sys.stdin.readline
INF = 1e9

def dijkstra(arr, S, exception):
    distance = [INF] * len(arr)
    pq = [(0, S)]
    distance[S] = 0
    
    while pq:
        value, current = heapq.heappop(pq)
        if distance[current] < value:
            continue
        for next_value, next in arr[current]:
            cost = value + next_value
            if distance[next] > cost and (current, next) not in exception:
                distance[next] = cost
                heapq.heappush(pq, (cost, next))
    return distance

def bfs(rev_arr, S, D, distance):
    q = deque([D])
    exception = set()

    while q:
        front = q.popleft()
        if front == S:
            continue
        for cost, prev in rev_arr[front]:
            if (prev, front) in exception:
                continue
            if cost + distance[prev] == distance[front]:
                exception.add((prev, front))
                q.append(prev)
    return exception

while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    S, D = map(int, input().split())
    
    arr = [list() for _ in range(N)]
    rev_arr = [list() for _ in range(N)]
    exception = set()
    for _ in range(M):
        U, V, P = map(int, input().split())
        arr[U].append((P, V))
        rev_arr[V].append((P, U))
    
    distance = dijkstra(arr, S, exception)
    exception = bfs(rev_arr, S, D, distance)
    distance = dijkstra(arr, S, exception)
    if distance[D] == INF:
        print(-1)
    else:
        print(distance[D])
