n = int(input())

# DP
a1 = 0
a2 = 1
if n < 2:
    print(n)
else:
    for i in range(2, n+1):
        result = a1 + a2
        a1 = a2
        a2 = result
    print(result)
    