N = int(input())

def hanoi(n, source, tmp, target, memo):
    if n == 1:
        memo.append((source, target))
        return 1

    cnt = 1
    cnt += hanoi(n-1, source, target, tmp, memo)
    memo.append((source, target))
    cnt += hanoi(n-1, tmp, source, target, memo)
    return cnt

memo = []
print(hanoi(N, 1, 2, 3, memo))
for x, y in memo:
    print(x, y)