import sys
input=sys.stdin.readline

T = int(input())

for _ in range(T):
    # a, b = map(int, input().split())
    # a %= 10
    # if a == 0:
    #     print(10)
    # if a in [1, 5, 6]:
    #     print(a)
    # if a == 2:
    #     b = (b%4)-1
    #     print([2,4,8,6][b])
    # if a == 3:
    #     b = (b%4)-1
    #     print([3,9,7,1][b])
    # if a == 4:
    #     b = (b%2)-1
    #     print([4, 6][b])
    # if a == 7:
    #     b = (b%4)-1
    #     print([7,9,3,1][b])
    # if a == 8:
    #     b = (b%4)-1
    #     print([8,4,2,6][b])
    # if a == 9:
    #     b = (b%2)-1
    #     print([9,1][b])
    
    a, b = map(int, input().split())
    result = pow(a, b, 10)
    if result == 0:
        print(10)
    else:
        print(result)
