N = int(input())

runner = 1
while True:
    if runner >= N:
        print(0)
        break
    arr = [runner]
    while runner > 0:
        arr.append(runner % 10)
        runner //= 10
    
    if sum(arr) == N:
        print(arr[0])
        break

    runner = arr[0]+1
