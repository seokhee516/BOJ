import sys 
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

# chance = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x=0, y=0, chance=1):
    q = deque()
    q.append((x,y,chance))
    visited[x][y][1] = 1
    while q:
        x, y, chance = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and visited[nx][ny][chance]==0:
                if graph[nx][ny] == 0:
                    q.append((nx,ny,chance))
                    visited[nx][ny][chance] = visited[x][y][chance] + 1
                if chance == 1 and graph[nx][ny] == 1:
                    q.append((nx,ny,0))
                    visited[nx][ny][0] = visited[x][y][chance] + 1
    return visited[N-1][M-1][chance]
answer = bfs()
if answer == 0:
    print(-1)
else:
    print(answer)