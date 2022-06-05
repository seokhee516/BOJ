import sys
input = sys.stdin.readline
from collections import deque

# 맵의 크기를 N 입력
n = int(input())
# 아기상어 크기
now_size = 2
# 모든 칸에 대한 정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        # 아기 상어 위치
        if array[i][j] == 9:
            now_x, now_y = i,j
            # 아무것도 없다고 처리
            array[i][j] = 0

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최단 경로 구하기
def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((now_x,now_y))
    # 시작 위치는 도달 가능, 거리는 0
    dist[now_x][now_y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 안에 있는 경우
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                # 자신의 크기보다 작거나 같은 경우 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))
    # 최단 거리 테이블 반환
    return dist

INF = 1e9
# 최단 거리가 주어졌을 때 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일때
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF: # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return x, y, min_dist # 먹을 물고기의 위치와 최단 거리

result = 0 # 최종 답안
ate = 0 # 현재 크기에서 먹은 양

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 아무것도 없도록 처리
        array[now_x][now_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0
        