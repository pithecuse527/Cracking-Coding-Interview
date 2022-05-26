import sys
input = sys.stdin.readline
N = int(input())
words = [input()[:-1] for _ in range(N)]
words.sort()
cnt = 0 
for i in range(N):
    flg = True
    for j in range(i+1, N):
        if words[j].startswith(words[i]):
            flg = False
            break
    if flg:
        cnt += 1
print(cnt)
