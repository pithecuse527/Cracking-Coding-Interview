N = int(input())

sing_num = 1
cnt = 0

while N > 0:
    if sing_num > N:
        sing_num = 1
    N -= sing_num
    sing_num += 1
    cnt += 1
print(cnt)