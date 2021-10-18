def solution(str):
    answer = int(str[0])
    for i in range(1, len(str)):
        if answer <= 1 or int(str[i]) <= 1:
            answer += int(str[i])
        else:
            answer *= int(str[i])
    return answer

def main():
    test_string = input()
    print(solution(test_string))

if __name__ == '__main__':
    main()
