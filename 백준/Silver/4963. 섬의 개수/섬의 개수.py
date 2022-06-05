import sys
input = sys.stdin.readline
from collections import deque

while True:
    # 너비와 높이 입력
    w,h = map(int, input().split())
    if w==0 and h==0:
        break
    # 섬의 정보 입력
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    # 이동할 방향 정의(가로, 세로, 대각선)
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))

        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < h and ny >= 0 and ny < w:
                    # 섬이 존재하면
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        queue.append((nx,ny))
                    
    cnt = 0 # 섬의 개수
    for x in range(h):
        for y in range(w):
            # 섬이 존재하면 bfs 탐색
            if graph[x][y] == 1:
                bfs(x,y)
                cnt += 1

    print(cnt)