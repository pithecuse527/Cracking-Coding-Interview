import sys

N = int(sys.stdin.readline())

lst = []
lst2 = []

def mergeSort(lst):
    if len(lst) > 1:
        m = len(lst)//2
        l = lst[:m]
        r = lst[m:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                lst[k] = l[i]
                i += 1
            else:
                lst[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            lst[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            lst[k] = r[j]
            j += 1
            k += 1

for _ in range(N):
    data = int(sys.stdin.readline())
    lst.append(data)
    lst2.append(data)

lst.sort()
mergeSort(lst2)
print()
for i in lst:
    print(i)

print()
for i in lst2:
    print(i)
