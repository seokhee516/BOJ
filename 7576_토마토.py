import sys 
from collections import deque
from collections import Counter
input = sys.stdin.readline
M, N = map(int, input().split())
graph = []
data = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    # 익은 토마토의 위치를 저장
    for j in range(M):
        if graph[i][j] == 1:
            data.append((0,i,j))
# 익지 않은 토마토의 수를 세는 함수
def get_tomato():
    tomato = 0
    for g in graph:
        tomato += Counter(g)[0]
    return tomato

q = deque(data)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while q:
    t, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((t+1, nx, ny))
# 모두 다 익었으면
if get_tomato() == 0:
    # 시간 출력
    print(t)
# 그렇지 않으면
else:
    # -1 출력
    print(-1)