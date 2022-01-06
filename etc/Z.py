def dfs(n, r, c):
    global cnt
    if n == 2:
        if r == X and c == Y:
            print(cnt)
            return
        cnt += 1
        if r == X and c + 1 == Y:
            print(cnt)
            return
        cnt += 1
        if r + 1 == X and c == Y:
            print(cnt)
            return
        cnt += 1
        if r + 1 == X and c + 1 == Y:
            print(cnt)
            return
        cnt += 1
        return

    dfs(n//2, r, c)
    dfs(n//2, r, c+n//2)
    dfs(n//2, r+n//2, c)
    dfs(n//2, r+n//2, c+n//2)

cnt = 0
N, X, Y = map(int, input().split())
dfs(2**N, 0, 0)
