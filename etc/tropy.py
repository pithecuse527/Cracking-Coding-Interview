N = int(input())

tropies = []
for _ in range(N):
    tropies.append(int(input()))

# left side
left_cnt = 0
left_max = -1
for i in range(N):
    if left_max < tropies[i]:
        left_cnt += 1
        left_max = tropies[i]

# right side
right_cnt = 0
right_max = -1
for i in range(N-1, -1, -1):
    if right_max < tropies[i]:
        right_cnt += 1
        right_max = tropies[i]

print(left_cnt)
print(right_cnt)