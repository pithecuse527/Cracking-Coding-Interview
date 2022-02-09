N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

def gcd_euclidean(a, b):
    if b == 0:
        return a
    return gcd_euclidean(b, a%b)

gcd = numbers[1] - numbers[0]
for i in range(2, len(numbers)):
    gcd = gcd_euclidean(gcd, numbers[i]-numbers[i-1])

answer = set()
for i in range(2, int(gcd**0.5)+1):
    if gcd % i == 0:
        answer.add(i)
        answer.add(gcd//i)
answer.add(gcd)

for i in sorted(answer):
    print(i, end=" ")
print()