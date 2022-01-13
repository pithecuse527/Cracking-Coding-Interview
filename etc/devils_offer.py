import math
from decimal import *

# K, N = map(float, input().split())    # error!
K, N = map(Decimal, input().split())    # more precise

if N == 1:
    print(-1)
else:
    print(math.ceil((K * N) / (N - 1)))