from collections import Counter
T = int(input())

for _ in range(T):
    s1, s2 = input().split()
    if len(s1) != len(s2):
        print("{} & {} are NOT anagrams.".format(s1, s2))
        continue
    s1_counts = Counter(s1)
    for c in s2:
        s1_counts[c] = s1_counts.get(c, 0) - 1

    for k, v in s1_counts.items():
        if v > 0 or v < 0:
            print("{} & {} are NOT anagrams.".format(s1, s2))
            break
    else:
        print("{} & {} are anagrams.".format(s1, s2))
