from collections import Counter

def solution(test_lst, n):
    answer = 0
    test_lst.sort()
    counts = Counter(test_lst)

    for i in counts:
        n -= counts[i]
        answer += n * counts[i]
    return answer

def main():
    test_lst = list(map(int, input().split()))
    print(solution(test_lst, len(test_lst)))

if __name__ == '__main__':
    main()
