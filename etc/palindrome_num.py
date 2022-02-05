while True:
    num = input()
    if num == '0':
        break
    
    # two pointers
    for i in range(len(num)):
        l = i
        r = len(num)-i-1
        if num[l] != num[r]:
            print('no')
            break
    else:
        print('yes')
