T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    S = input()

    answer = 0
    for i in range(N//2):
        if S[i] != S[-1-i]:
            answer += 1

    print('Case #{}: {}'.format(str(_+1), str(abs(answer - K))))
