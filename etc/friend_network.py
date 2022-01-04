test_cases = int(input())

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    # when the most top parent is different,
    # it means the two nodes are in the different set
    if x != y:
        parent[y] = x
        number[x] += number[y]
        number[y] += number[x]

for _ in range(test_cases):
    parent = dict()
    number = dict()

    for i in range(int(input())):
        f1, f2 = input().split()
        if f1 not in parent:
            parent[f1] = f1
            number[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1
        union(f1, f2)
        print(number[find(f1)])
