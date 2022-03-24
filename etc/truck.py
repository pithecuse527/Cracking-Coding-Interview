from collections import deque
import sys
input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
time = 0
bridge = deque([0]*W)
curr_weight = 0
while trucks:
    time += 1
    curr_weight -= bridge.popleft()
    if curr_weight + trucks[0] <= L:
        curr_weight += trucks[0]
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)

while bridge:
    time += 1
    bridge.popleft()
    
print(time)