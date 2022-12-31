from collections import deque
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = [list(input().strip()) for _ in range(m)]
w_score = 0
b_score = 0
# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# BFS 소스코드 구현
def bfs(x, y, c):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    cnt = 0 # 병사의 수
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        cnt += 1
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == c:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return cnt
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            w_score += bfs(i, j, 'W')**2
        if graph[i][j] == 'B':
            b_score += bfs(i, j, 'B')**2
print(w_score, b_score)
