from collections import deque
import sys
input = sys.stdin.readline

# 입력값 받는 과정
n = int(input())
c1, c2 = map(int, input().split())
m = int(input())
adj = [list() for _ in range(n+1)]
degree = [0] * (n+1)

# 두 노드를 연결하되 양방향으로 연결 (위아래 구분 X)
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

q = deque([c1])  # c1으로 시작하든 c2로 시작하는 상관 없음
visited = set()  # bfs를 돌며 방문한 노드 기록
while q:  # bfs
    front = q.popleft()
    visited.add(front)
    
    for next in adj[front]:
        if next not in visited:
            visited.add(next)
            q.append(next)
            degree[next] = degree[front]+1  # 다음에 방문할 노드의 촌수 == 현재 방문한 촌수(front) + 1
if degree[c2] > 0:  # 만약 친척이라면,
    print(degree[c2])
else:  # 친척이 아니면
    print(-1)