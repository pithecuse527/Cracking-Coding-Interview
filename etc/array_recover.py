import sys, copy
input = sys.stdin.readline
H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]
A = copy.deepcopy(B)

for i in range(X, H):
    for j in range(Y, W):
        A[i][j] = B[i][j]-A[i-X][j-Y]

for i in range(H):
    for j in range(W):
        print(A[i][j], end=' ')
    print()
