import sys
input = sys.stdin.readline

def gcd(x, y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

N = int(input())
lst = sorted(map(int, input().split()))
diff_lst = []
for i in range(1, N):
    diff_lst.append(lst[i]-lst[i-1])

ans = diff_lst[0]
for i in range(1, len(diff_lst)):
    ans = gcd(ans, diff_lst[i])
print(ans)
