from collections import deque
from re import L
import sys
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
floor  = [-1 for i in range(f)]
floor[s-1] = 0 # 지금 있는 층 방문
dir = [u, -d] # 방향
def bfs(i):
    q = deque()
    q.append(i)
    visited = [0 for i in range(f)]
    visited[i] = 1
    while q:
        x = q.popleft()
        for i in range(2): # 위 아래 방향 확인
            nx = x + dir[i]
            if 0 <= nx < f and visited[nx] == 0:
                q.append(nx)
                floor[nx] = floor[x] + 1 # 이전 층 누른 횟수 더하기
                visited[nx] = 1 # 방문 표시
bfs(s-1) # 지금 있는 층에서 시작
if floor[g-1] != -1: # g층에 도착했다면
    print(floor[g-1]) # 버튼 누르는 횟수 출력
else:
    print("use the stairs")