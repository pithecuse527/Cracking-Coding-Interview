def solution(A, B):
    # write your code in Python 3.6
    answer = []
    while A or B:
        if len(answer) >= 2 and answer[-1] == answer[-2]:
            writeA = answer[-1] == 'b'
        else:
            writeA = A >= B
        
        if writeA:
            answer.append('a')
            A -= 1
        else:
            answer.append('b')
            B -= 1
    return "".join(answer)
