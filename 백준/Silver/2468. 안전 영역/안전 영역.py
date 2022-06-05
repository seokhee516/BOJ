import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

# 높이 정보 입력
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# 안전영역 표시할 그래프
graph = [[False]*n for i in range(n)]

# 이동할 방향 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_safe(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == True: # 안전영역이라면
                    graph[nx][ny] = False # 주변지역 방문
                    queue.append((nx,ny))

max_value = max(max(data)) # 최대높이
result = 0 # 안전영역 개수
temp = 0

# 높이가 k 이하인 지점 모두 잠길때 안전 영역 표시 
for k in range(max_value, -1, -1): # 높은 곳부터 비가 오지 않았을 때까지(0) 확인
    for i in range(n):
        for j in range(n):
            if data[i][j] > k: # 지역이 비 높이보다 높다면
                graph[i][j] = True # 안전영역 표시
    # 안전영역 개수 세기
    for i in range(n):
        for j in range(n):
            if graph[i][j]: # 안전영역이면서 방문한적 없다면
                get_safe(i,j)
                temp += 1
    result = max(result, temp)
    temp = 0


print(result)