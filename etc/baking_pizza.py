import sys
input = sys.stdin.readline
D, N = map(int, input().split())
oven = [0] + list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(1, D):
    oven[i+1] = min(oven[i], oven[i+1])

pizza_runner = 0
depth = 0
for i in range(D, 0, -1):
    if pizza_runner >= N:
        break
    if pizza[pizza_runner] <= oven[i]:
        pizza_runner += 1
        depth = i
if pizza_runner >= N:
    print(depth)
else:
    print(0)
