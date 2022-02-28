import sys
input = sys.stdin.readline
N = int(input())
switches = [0]+list(map(int, input().split()))
M = int(input())
students = []

for _ in range(M):
    students.append(tuple(map(int, input().split())))

for gender, idx in students:
    if gender == 1:
        for i in range(idx, N+1, idx):
            switches[i] ^= 1
    else:
        # two pointers
        switches[idx] ^= 1
        left = idx-1
        right = idx+1
        while left > 0 and right < N+1:
            if switches[left] == switches[right]:
                switches[left] = switches[right] = switches[left]^1
                left -= 1
                right += 1
            else:
                break

for i in range(1, N+1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print()
print()
