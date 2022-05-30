import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
rank = [0] * (N+1)

def find(city):
    if city != parent[city]:
        parent[city] = find(parent[city])
    return parent[city]

def union(city1, city2):
    city1_root = find(city1)
    city2_root = find(city2)

    if rank[city1_root] < rank[city2_root]:
        parent[city1_root] = city2_root
    else:
        parent[city2_root] = city1_root
        if rank[city1_root] == rank[city2_root]:
            rank[city1_root] += 1

for i in range(1, N+1):
    connection = list(map(int, input().split()))
    for j in range(1, len(connection)+1):
        if connection[j-1] == 1:
            union(i, j)

travel = list(map(int, input().split()))
target = find(travel[0])
flg = True
for i in range(1, len(travel)):
    if target != find(travel[i]):
        flg = False
        break
print('YES' if flg else 'NO')
