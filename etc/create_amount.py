def solution(test_lst):
    test_lst.sort()
    target = 1
    
    for num in test_lst:
        if target < num:
            break
        target += num
        
    return target

def main():
    test_lst = list(map(int, input().split()))
    print(solution(test_lst))

if __name__ == '__main__':
    main()
