def rangeFinder(n, r, c, cnt):
    global X, Y
    if n == 2:
        for i in range(r, r+2):
            for j in range(c, c+2):
                if i == X and j == Y:
                    print(cnt)
                    return
                cnt += 1
        return

    if X < r + n//2 and Y < c + n//2:
        rangeFinder(n//2, r, c, cnt)
    elif X < r + n//2 and Y >= c + n//2:
        rangeFinder(n//2, r, c+n//2, cnt + (n//2)**2)
    elif X >= r + n//2 and Y < c + n//2:
        rangeFinder(n//2, r+n//2, c, cnt + (n//2)**2 * 2)
    else:
        rangeFinder(n//2, r+n//2, c+n//2, cnt + (n//2)**2 * 3)

# def dfs(n, r, c):
#     global cnt
#     if n == 2:
#         if r == X and c == Y:
#             print(cnt)
#             return
#         cnt += 1
#         if r == X and c + 1 == Y:
#             print(cnt)
#             return
#         cnt += 1
#         if r + 1 == X and c == Y:
#             print(cnt)
#             return
#         cnt += 1
#         if r + 1 == X and c + 1 == Y:
#             print(cnt)
#             return
#         cnt += 1
#         return

#     dfs(n//2, r, c)
#     dfs(n//2, r, c+n//2)
#     dfs(n//2, r+n//2, c)
#     dfs(n//2, r+n//2, c+n//2)

N, X, Y = map(int, input().split())
# dfs(2**N, 0, 0)
rangeFinder(2**N, 0, 0, 0)