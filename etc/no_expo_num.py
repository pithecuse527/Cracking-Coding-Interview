import sys
input = sys.stdin.readline
min_, max_ = map(int, input().split())

nums = max_ - min_ + 1
visited = set()
i = 2

while i*i <= max_:
    pow_ = i*i
    operand = min_ // pow_
    while operand * pow_ < min_:
        operand += 1
    
    tmp = operand * pow_
    while tmp <= max_:
        if tmp not in visited:
            nums -= 1
            visited.add(tmp)
        operand += 1
        tmp = operand * pow_
    i += 1
print(nums)