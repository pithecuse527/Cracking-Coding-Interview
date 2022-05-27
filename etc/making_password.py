import sys, copy
input = sys.stdin.readline
L, C = map(int, input().split())
chars = sorted(input().split())
vowels = {'a', 'e', 'i', 'o', 'u'}

def print_passwd(collection):
    for a in sorted(collection):
        print(a, end='')
    print()

def dfs(collection, idx):
    if len(collection) == L:
        collection_vowels = collection & vowels
        collection_consonants = collection - collection_vowels
        if collection_vowels and len(collection_consonants) >= 2:
            print_passwd(collection)
        return
    if idx >= C:
        return
    
    collection.add(chars[idx])
    dfs(collection, idx+1)
    collection.discard(chars[idx])
    dfs(collection, idx+1)

dfs(set(), 0)
