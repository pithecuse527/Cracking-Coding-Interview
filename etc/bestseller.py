N = int(input())

hash = dict()
for _ in range(N):
    album = input()
    hash[album] = hash.get(album, 0) + 1

result = max(hash.items(), key=lambda x:x[1])
print(result[0])