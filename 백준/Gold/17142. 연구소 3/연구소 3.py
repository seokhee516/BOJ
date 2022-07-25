# 조합으로 방문할 수 있는 모든 경우를 찾고
# 방문한 시간을 visited를 통해 저장 하는게 포인트!!!
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
INF = 1e9
# 연구소 크기 n, 바이러스 개수 m
n, m = map(int, input().split())
wall_cnt = 0 # 벽의 개수
virus = [] # 바이러스 위치 저장 리스트 
# 연구소 초기 맵 리스트
graph = []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(n):
        if line[j] == 1:
            wall_cnt += 1 # 벽의 개수 세기
        elif line[j] == 2:
            virus.append((i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(active):
    q = deque()
    visited = [[-1]*n for _ in range(n)] # 방문 시간 표시
    res = 0 # 바이러스 퍼뜨리는 시간 저장
    for x, y in active: # 활성화된 부분 방문 표시 -> 이 부분이 포인트
        q.append((x,y))
        visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 0 and visited[nx][ny] == -1: # 빈 공간이고 첫 방문이면
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1 # 이전 방문한 시간에서 1 더해줌 
                    res = max(res, visited[nx][ny]) # 큰 값 저장
                # 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
                elif graph[nx][ny] == 2 and visited[nx][ny] == -1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    # sum(visited, []) 리스트를 한줄로 합치는 방법!
    if sum(visited, []).count(-1) != wall_cnt: # 다 방문했다면 벽의 개수 같음 
        return INF # 다르다면 방문하지 못함
    return res


ans = INF
# 방문할 수 있는 모든 조합 만들기
for active in combinations(virus,m): # virus의 요소들로 m개만큼 만듦
    ans = min(ans, bfs(active))
if ans != INF:
    print(ans)
else:
    print(-1)
