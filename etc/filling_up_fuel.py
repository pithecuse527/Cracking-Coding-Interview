import sys, heapq
input = sys.stdin.readline
N = int(input())
gas_station = [tuple(map(int, input().split())) for _ in range(N)]
gas_station.sort(reverse=True)
L, P = map(int, input().split())

curr_loc = 0
curr_gas = P
q = []
cnt = 0
while curr_loc+curr_gas < L:
    while gas_station and curr_loc+curr_gas >= gas_station[-1][0]:
        loc, fuel = gas_station.pop()
        heapq.heappush(q, (-fuel, loc))
    
    if not q:
        cnt = -1
        break

    next_fuel, next_loc = heapq.heappop(q)
    curr_gas = curr_gas - (next_loc - curr_loc) - next_fuel
    curr_loc = next_loc
    cnt += 1
print(cnt)