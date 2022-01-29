N = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers.sort()
runner1 = 0
runner2 = len(numbers)-1

cnt = 0
while runner1 < runner2:
    tmp_sum = numbers[runner1]+numbers[runner2]
    if tmp_sum == x:
        cnt += 1
        runner1 += 1
        runner2 -=1
    elif tmp_sum > x:
        runner2 -= 1
    else:
        runner1 += 1
print(cnt)