import sys
input = sys.stdin.readline
N = int(input())
words = [input() for _ in range(N)]

cnt = 0
for word in words:
    runner = 0
    visited = set()
    flg = True
    while runner < len(word):
        if word[runner] in visited:
            flg = False
            break
        if word[runner] not in visited:
            c = word[runner]
            visited.add(c)
            while runner < len(word) and word[runner] == c:
                runner += 1
    if flg:
        cnt += 1
print(cnt)