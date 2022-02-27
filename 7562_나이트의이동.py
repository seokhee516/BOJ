from collections import deque
import sys
input = sys.stdin.readline

# 나이트 이동할 방향 정의 8방향
dx = [-2,-2,-1,-1,2,2,1,1]
dy = [-1,1,-2,2,-1,1,-2,2]
# BFS
def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        # 현재 칸이 이동하려는 칸이면 최단 거리 리턴
        if x == t_x and y == t_y:
            return graph[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < I and ny >= 0 and ny < I:
                # 방문하지 않은 칸이라면
                if graph[nx][ny] == -1:
                    # 최단 거리 갱신
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
# 테스트 케이스 개수
T = int(input())
for _ in range(T):
    # 체스판 한 변의 길이
    I = int(input())
    # I x I 체스판 그래프
    graph = [[-1] * I for _ in range(I)]
    # 나이트가 현재 있는 칸
    x, y = map(int, input().split())
    # 나이트가 이동하려고 하는 칸
    t_x, t_y = map(int, input().split())
    # 현재 칸 0으로 시작
    graph[x][y] = 0
    print(bfs(x,y))