from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
graph = [] # 시헙관 상태 저장 그래프
data = [] # 바이러스의 상태 저장
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            # 바이러스의 종류, 시간, 위치
            data.append((graph[i][j],0,i,j))
S, X, Y = map(int, input().split())

'''
data = [(1, 0, 0, 0), (2, 0, 0, 2), (3, 0, 2, 0)]
'''
# 번호가 낮은 순으로 정렬
data.sort()
# 큐에 바이러스 상태 넣기
q = deque(data)

# 상하좌우 확인
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# BFS
while q:
    v, t, x, y = q.popleft()
    # 시간이 S초 일때 멈추기
    if t == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            # 바이러스 존재하지 않는다면
            if graph[nx][ny] == 0:
                # 전염
                graph[nx][ny] = v
                # 큐에 바이러스 상태 저장
                q.append((graph[nx][ny],t+1,nx,ny))
    
print(graph[X-1][Y-1])