lst = list(map(int, input().split()))

asc = True
dec = True
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        asc = False
    elif lst[i] < lst[i+1]:
        dec = False
if asc and not dec:
    print("ascending")
elif dec and not asc:
    print("descending")
else:
    print("mixed")
