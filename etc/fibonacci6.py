import sys
input = sys.stdin.readline

def mat_mul(A, B):
    An = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                An[i][j] += A[i][k]*B[k][j]
            An[i][j] %= 1000000007
    return An

def pow(A, n):
    if n == 1:
        return A
    else:
        tmp = pow(A, n//2)
        if n % 2 == 0:
            return mat_mul(tmp, tmp)
        else:
            return mat_mul(mat_mul(tmp, tmp), A)

N = int(input())
A = [[1, 1], [1, 0]]
print(pow(A, N)[0][1])
