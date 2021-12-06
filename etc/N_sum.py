def solve(a: list) -> int:
    to_return = 0
    for i in range(len(a)//2):
        to_return += a[i] + a[-1-i]
    if len(a) % 2 == 0:
        return to_return
    return to_return + a[len(a)//2]

print(solve([1,2,3,4,5,6,7]))

