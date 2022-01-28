N = int(input())

C = list(map(int, input().split()))
sorted_C = sorted(set(C))
hash_C = {sorted_C[i]:i for i in range(len(sorted_C))}

for c in C:
    print(hash_C[c], end=' ')
print()