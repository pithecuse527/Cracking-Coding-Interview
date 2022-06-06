from collections import deque
import sys
input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    dp = [[[0]*W for h in range(H)] for k in range(K+1)]
    normal_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    horse_dirs = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

    while q:
        ck, cy, cx = q.popleft()
        if cy == H-1 and cx == W-1:
            return dp[ck][cy][cx]
        for dy, dx in normal_dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < H and 0 <= nx < W) or dp[ck][ny][nx] != 0 or board[ny][nx] == 1:
                continue
            q.append((ck, ny, nx))
            dp[ck][ny][nx] = dp[ck][cy][cx] + 1
        if ck < K:
            for dy, dx in horse_dirs:
                ny, nx = dy+cy, dx+cx
                if not (0 <= ny < H and 0 <= nx < W) or dp[ck+1][ny][nx] != 0 or board[ny][nx] == 1:
                    continue
                q.append((ck+1, ny, nx))
                dp[ck+1][ny][nx] = dp[ck][cy][cx] + 1
    return -1

print(bfs())
        