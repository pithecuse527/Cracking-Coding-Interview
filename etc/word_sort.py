N = int(input())

words = set()
for _ in range(N):
    words.add(input())

words_array = sorted(words, key=lambda x:(len(x), x))
for w in words_array:
    print(w)
