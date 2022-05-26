import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]
q = deque([])

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))
        for k in range(m):
            if graph[i][j][k] == 1:
                # 인풋과 함께 바로 큐에 넣기 
                # 익은 토마토의 순서가 생기지 않게 하기 위해
                q.append((i,j,k))

# 이동할 방향 정의 
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 토마토 익히기 위한 bfs
def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 맵 안에 있는 경우
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    q.append((nx, ny, nz))
# 토마토 익히기
bfs()

# 며칠이 걸리는지 계산하여 출력
def process():
    max_time = -1
    for i in range(h):
        for j in range(n):
            # 안익은 토마토 있다면 -1 출력
            if 0 in graph[i][j]:
                return -1
            # 익은 토마토 첫날이 1부터 시작하므로 -1 해주기
            max_time = max(max_time, max(graph[i][j])-1)
    return max_time
print(process())