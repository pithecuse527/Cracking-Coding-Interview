def solution(str):
    cnt1 = 0
    cnt2 = 0
    
    for i in range(len(str)-1):
        if str[i] == '0' and str[i+1] == '1':
            cnt1 += 1
        if str[i] == '1' and str[i+1] == '0':
            cnt2 += 1
        
    # reamining part
    if str[-1] == '0':
        cnt1 += 1
    if str[-1] == '1':
        cnt2 += 1

    return cnt1 if cnt1 < cnt2 else cnt2

def main():
    test_str = input()
    print(solution(test_str))

if __name__ == '__main__':
    main()
