import sys
input = sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))
dp = [seq[0]]

for i in range(1, N):
    dp.append(max(seq[i], dp[-1]+seq[i]))
print(dp)
