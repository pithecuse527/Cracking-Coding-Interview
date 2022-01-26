N = int(input())

coordinates = []
for _ in range(N):
    c = tuple(map(int, input().split()))
    coordinates.append(c)
coordinates.sort(key=lambda x : (x[1], x[0]))

for i in coordinates:
    print(i[0], i[1])
