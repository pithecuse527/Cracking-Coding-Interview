import sys
input = sys.stdin.readline

def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

accum = 0
cnt = 0
for num in arr:
    if euclidean_gcd(num, X)==1:
        accum += num
        cnt += 1
print(accum/cnt)
