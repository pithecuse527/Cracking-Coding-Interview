import sys
input = sys.stdin.readline

N = int(input())

queen_loc = [-1]*N
cnt = 0
def promising(lv):
    for i in range(lv):
        if queen_loc[i] == queen_loc[lv] or (lv-i == abs(queen_loc[lv]-queen_loc[i])):
            return False
    return True

def nQueen(lv):
    global cnt
    if lv == N:
        cnt += 1
        return

    for i in range(N):
        queen_loc[lv] = i
        if promising(lv):
            nQueen(lv+1)
nQueen(0)
print(cnt)