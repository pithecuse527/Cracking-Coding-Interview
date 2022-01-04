N = int(input())
hash = set(map(int, input().split()))

M = int(input())
lst2 = list(map(int, input().split()))
for i in lst2:
    if i in hash:
        print(1)
    else:
        print(0)
