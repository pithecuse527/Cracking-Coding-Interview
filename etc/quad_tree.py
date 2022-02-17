N = int(input())

image = [input() for _ in range(N)]

def compress(sy, sx, ey, ex):
    pvt = image[sy][sx]
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            if pvt != image[y][x]:
                return -1
    return pvt

def divide(sy, sx, ey, ex, size):
    compressed = compress(sy, sx, ey, ex)
    if compressed != -1:
        print(compressed, end='')
    else:
        print('(', end='')
        half = size // 2
        divide(sy, sx, sy+half-1, sx+half-1, half)
        divide(sy, sx+half, sy+half-1, ex, half)
        divide(sy+half, sx, ey, sx+half-1, half)
        divide(sy+half, sx+half, ey, ex, half)
        print(')', end='')

divide(0, 0, N-1, N-1, N)
print()