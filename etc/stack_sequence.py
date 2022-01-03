n = int(input())

count = 1
stk = []
result = []

for i in range(n):
    data = int(input())
    while count <= data:    # next push item should be lower than the data
        stk.append(count)
        count += 1
        result.append('+')  
    if stk[-1] == data:     # if the order is right, pop it
        stk.pop()
        result.append('-')
    else:       # if not, return 'no'
        print("NO")
        exit(0)
print('\n'.join(result))
