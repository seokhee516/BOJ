import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())
graph = [[True] * (n) for _ in range(m)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for y in range(ly,ry):
        for x in range(lx, rx):
            graph[y][x] = False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def get_sum(x,y):
    cnt = 1
    graph[x][y] = False
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[nx][ny]:
                    graph[nx][ny] = False
                    cnt += 1
                    queue.append((nx,ny))
    return cnt

res = 0
res_array = []
for i in range(m):
    for j in range(n):
        if graph[i][j]:
            res += 1
            res_array.append(get_sum(i,j))
print(res)
res_array.sort()
for r in res_array:
    print(r, end =' ')