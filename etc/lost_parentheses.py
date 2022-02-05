expr = input().split('-')

res = 0
for e1 in map(int, expr[0].split('+')):
    res += e1

for e2 in expr[1:]:
    for n in map(int, e2.split('+')):
        res -= n
print(res)
