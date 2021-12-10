import math
from collections import Counter

N = int(input())
integers = []

for i in range(N):
    integers.append(int(input()))
integers.sort()

tmp = Counter(integers).most_common()
freq = 0
if len(tmp) > 1:
    if tmp[0][1] == tmp[1][1]:
        freq = tmp[1][0]
    else:
        freq = tmp[0][0]
else:
    freq = tmp[0][0]
print()
print(round(sum(integers)/N))
print(integers[N//2])
print(freq)
print(integers[-1]-integers[0])
