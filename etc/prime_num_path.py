import sys
from collections import deque
input = sys.stdin.readline

def prime_lst():
    sieve = [True]*10000
    for i in range(2, int(10000**0.5)+1):
        if sieve[i]:
            for j in range(i+i, 10000, i):
                sieve[j] = False
    return set([i for i in range(2, 10000) if sieve[i]])

def bfs(A, B, primes):
    q = deque([str(A)])
    visited = [-1]*10000
    visited[A] = 0
    num_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while q:
        curr = q.popleft()
        for i in range(4):
            curr_str = list(curr)
            for c in num_chars:
                curr_str[i] = c
                tmp = int(''.join(curr_str))
                if tmp >= 1000 and tmp in primes and visited[tmp] == -1:
                    visited[tmp] = visited[int(curr)]+1
                    q.append(str(tmp))
    return visited[B] if visited[B] >= 0 else 'Impossible'

T = int(input())
primes = prime_lst()
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B, primes))
