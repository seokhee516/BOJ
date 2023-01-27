import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip().split()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
def bfs(x,y):
    res = 0
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        graph[x][y] = '0'
        res += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1':
                graph[nx][ny] = '0'
                q.append((nx,ny))
    return res
cnt = 0
size = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            cnt += 1
            size = max(size, bfs(i,j))

print(cnt)
print(size)