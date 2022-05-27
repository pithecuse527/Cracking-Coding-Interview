import sys, copy
input = sys.stdin.readline
N = int(input())
bulbs_ori = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

def change(bulbs, i):
    if i-1 >= 0:
        bulbs[i-1] ^= 1
    bulbs[i] ^= 1
    if i+1 < N:
        bulbs[i+1] ^= 1

def check(bulbs):
    for i in range(len(bulbs)):
        if bulbs[i] != target[i]:
            return False
    return True

# touching first light bulb
bulbs = copy.deepcopy(bulbs_ori)
bulbs[0] ^= 1
bulbs[1] ^= 1
cnt1 = 1
for i in range(1, N):
    if bulbs[i-1] != target[i-1]:
        change(bulbs, i)
        cnt1 += 1
if not check(bulbs):
    cnt1 = -1

# not touching first light bulb
bulbs = copy.deepcopy(bulbs_ori)
cnt2 = 0
for i in range(1, N):
    if bulbs[i-1] != target[i-1]:
        change(bulbs, i)
        cnt2 += 1
if not check(bulbs):
    cnt2 = -1

if cnt1 == cnt2:
    print(cnt1)
elif cnt1 != -1 and cnt2 == -1:
    print(cnt1)
elif cnt1 == -1 and cnt2 != -1:
    print(cnt2)
elif cnt1 < cnt2:
    print(cnt1)
else:
    print(cnt2)