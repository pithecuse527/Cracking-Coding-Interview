import sys
input = sys.stdin.readline
N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def mat_mul(mat1, mat2):
    result_matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result_matrix[i][j] += (mat1[i][k] * mat2[k][j])
                result_matrix[i][j] %= 1000
    return result_matrix

def mat_pow(matrix, b):
    if b == 0:
        return None
    if b == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= 1000
        return matrix

    half_mat_mul = mat_pow(matrix, b//2)
    remain_mat_mul = mat_pow(matrix, b%2)
    return mat_mul(mat_mul(half_mat_mul, half_mat_mul), remain_mat_mul) if remain_mat_mul else mat_mul(half_mat_mul, half_mat_mul)

result = mat_pow(matrix, B)
for i in range(N):
    for j in range(N):
        print(result[i][j], end=' ')
    print()
