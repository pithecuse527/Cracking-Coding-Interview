import heapq

N = int(input())

kor_scores = []
eng_scores = []
math_scores = []
sci_scores = []
awarded = set()
for _ in range(N):
    idx, kor, eng, math, sci = map(int, input().split())
    heapq.heappush(kor_scores, (-kor, idx))
    heapq.heappush(eng_scores, (-eng, idx))
    heapq.heappush(math_scores, (-math, idx))
    heapq.heappush(sci_scores, (-sci, idx))

while True:
    score, candidate = heapq.heappop(kor_scores)
    if candidate not in awarded:
        awarded.add(candidate)
        print(candidate, end=' ')
        break
while True:
    score, candidate = heapq.heappop(eng_scores)
    if candidate not in awarded:
        awarded.add(candidate)
        print(candidate, end=' ')
        break
while True:
    score, candidate = heapq.heappop(math_scores)
    if candidate not in awarded:
        awarded.add(candidate)
        print(candidate, end=' ')
        break
while True:
    score, candidate = heapq.heappop(sci_scores)
    if candidate not in awarded:
        awarded.add(candidate)
        print(candidate, end=' ')
        break
print()