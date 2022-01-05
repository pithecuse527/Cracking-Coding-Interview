N = int(input())

lst = []
for _ in range(N):
    age, name = input().split()
    lst.append((int(age), name))

# compare only with the first element, others will be stable
lst.sort(key=lambda x:x[0]) 

for i in lst:
    print(i[0], i[1])