import sys
input = sys.stdin.readline
N, M = map(int, input().split())
map_arr = [input() for _ in range(N)]
directions = [(0, 1), (0, -1), (1, 0), (-1,0)]
answer = 0

def dfs(y, x, visited_char, depth):
    global answer
    answer = max(depth, answer)

    for dy, dx in directions:
        ny = dy+y
        nx = dx+x
        if 0 <= ny < N and 0 <= nx < M:
            char_idx = ord(map_arr[ny][nx])-65
            if not visited_char[char_idx]:
                visited_char[char_idx] = True
                dfs(ny, nx, visited_char, depth+1)
                visited_char[char_idx] = False

visited_char = [False]*26
visited_char[ord(map_arr[0][0])-65] = True
dfs(0, 0, visited_char, 1)
print(answer)