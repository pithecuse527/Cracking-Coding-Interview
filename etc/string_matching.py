import sys, re
input = sys.stdin.readline
N = int(input())
s, e = input().rstrip().split("*")
reg = re.compile(s+'.*'+e+'+')

for i in range(N):
    s = input().rstrip()
    tmp = reg.search(s)
    if tmp and tmp.group() == s:
        print('DA')
    else:
        print('NE')
