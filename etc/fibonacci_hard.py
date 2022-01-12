T = int(input())

def fibo(n):
    memo = [(1, 0), (0, 1)]
    for i in range(2, n+1):
        x = memo[i-1][0] + memo[i-2][0]
        y = memo[i-1][1] + memo[i-2][1]
        memo.append((x, y))
    return memo[n]

for _ in range(T):
    n = int(input())
    result = fibo(n)
    print(result[0], result[1])
