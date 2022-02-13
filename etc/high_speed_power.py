A, B, C = map(int, input().split())

def mult(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b == 2:
        return (a*a)
    
    remainder = mult(a, b%2, c)
    half = mult(a, b//2, c)

    return (half * half * remainder) % c
print(mult(A, B, C))
