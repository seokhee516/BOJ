import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [] # 적록색약 아닌 사람 그래프
rg_graph = [[] for _ in range(n)] # 적록색약 그래프
for i in range(n):
    graph.append(list(map(str, input().strip())))
    rg_graph[i] = graph[i][:]
    for j in range(n):
        if rg_graph[i][j] =='G': # 적록색약 G를 R로 통일
            rg_graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
rgb, rg = 0, 0 # 적록색약 아닌 구역, 적록색약 구역 수

# 상하좌우 확인
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# bfs 진행
# x, y 좌표, 방문표시, 색, 그래프 종류 
def bfs(x, y, v, color, graph):
    q = deque()
    q.append((x, y))
    visited[x][y] += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                # 색이 같고 방문 하지 않았다면
                if graph[nx][ny] == color and visited[nx][ny] == v:
                    q.append((nx,ny))
                    # 방문 표시
                    visited[nx][ny] += 1

for x in range(n):
    for y in range(n):
        if visited[x][y] == 0: #적록 색약 아닌 사람 방문 하지 않음 0
            if graph[x][y] == 'B':
                rgb += 1
                bfs(x, y, 0, 'B', graph)
            if graph[x][y] == 'G':
                rgb += 1
                bfs(x, y, 0, 'G', graph)
            if graph[x][y] == 'R':
                rgb += 1
                bfs(x, y, 0, 'R', graph)

for x in range(n):
    for y in range(n):
        if visited[x][y] == 1: # 적록 색약 아닌 사람 방문 하지 않음 1
            if rg_graph[x][y] == 'B':
                rg += 1
                bfs(x, y, 1, 'B', rg_graph)
            if rg_graph[x][y] == 'R':
                rg += 1
                bfs(x, y, 1, 'R', rg_graph)

print(rgb, rg)