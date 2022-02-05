N = int(input())
edge = list(map(int, input().split()))
node = list(map(int, input().split()))

min_cost = node[0]
result = 0
for i in range(N-1):
    if node[i] < min_cost:
        min_cost = node[i]
    result += (min_cost * edge[i])
print(result)
