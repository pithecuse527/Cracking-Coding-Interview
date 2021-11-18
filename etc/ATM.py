N = int(input())
people = list(map(int, input().split()))

accumulate = 0
people.sort()
answer = 0

for p in people:
    answer += (p+accumulate)
    accumulate += p

print(answer)
