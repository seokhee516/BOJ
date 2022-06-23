import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[0] * m for i in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(graph, i, j):
    global answer
    cnt  = 1
    q = deque()
    q.append((i,j))
    graph[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    answer = max(answer, cnt)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(graph, i, j)
print(answer)