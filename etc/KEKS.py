import sys
input = sys.stdin.readline
N, K = map(int, input().split())
target_len = N-K
num = input()[:-1]

stk = []
answer = []
runner = 0

while runner < len(num):
    while stk and num[runner] > stk[-1] and K > 0:
        stk.pop()
        K -= 1
    stk.append(num[runner])
    runner += 1
    
while len(stk) != target_len:
    stk.pop()

print("".join(stk))
