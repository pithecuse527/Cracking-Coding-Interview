def solution(test_lst):
    test_lst.sort()
    cnt = 0
    answer = 0

    for p in test_lst:
        cnt += 1
        if cnt >= p:
            answer += 1
            cnt = 0
    return answer

def main():
    test_lst = list(map(int, input().split()))
    print(solution(test_lst))

if __name__ == '__main__':
    main()
