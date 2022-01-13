import math
from decimal import *

K, N = map(float, input().split())
getcontext().prec = 1500

if N == 1:
    print(-1)
else:
    print(math.ceil((K * N) / (N - 1)))