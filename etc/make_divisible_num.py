N = int(input())
F = int(input())

numb = N // 100
numb *= 100

while numb % F != 0:
    numb += 1
numb %= 100
if numb < 10:
    print(0, end='')
print(numb)