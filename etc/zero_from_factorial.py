N = int(input())

calculated = 1
for i in range(2, N+1):
    calculated *= i

str_calculated = str(calculated)
cnt = 0
for i in range(len(str_calculated)):
    if str_calculated[-1-i] != '0':
        break
    cnt += 1
print(cnt)
