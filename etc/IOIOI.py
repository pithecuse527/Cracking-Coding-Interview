import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
str = input()

runner = 1
ans = 0
sub_IOI = 0
while runner < M-1:
    if str[runner-1]=='I' and str[runner]=='O' and str[runner+1]=='I':
        sub_IOI += 1
        if sub_IOI == N:
            sub_IOI -= 1
            ans += 1
        runner = runner + 2
    else:
        sub_IOI = 0
        runner += 1
print(ans)