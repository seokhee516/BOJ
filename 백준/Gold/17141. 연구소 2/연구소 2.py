# 연구소 3 문제에서 살짝만 바꿔주면 됨!
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
            virus.append((i, j)) # 바이러스 위치 저장
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(v):
    q = deque()
    visited = [[-1]*n for _ in range(n)] # 방문 시간 표시
    res = 0 # 바이러스 퍼뜨리는 시간 저장
    for x, y in v: # 바이러스 방문 표시
        q.append((x,y))
        visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if (graph[nx][ny] == 0 or graph[nx][ny] == 2)and visited[nx][ny] == -1: # 빈 공간이거나 방문표시가 있고, 첫 방문이면
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1 # 이전 방문한 시간에서 1 더해줌 
                    res = max(res, visited[nx][ny]) # 큰 값 저장
    if sum(visited, []).count(-1) != wall_cnt: # 다 방문했다면 벽의 개수 같음 
        return INF # 다르다면 방문하지 못함
    return res


ans = INF
# 방문할 수 있는 모든 조합 만들기
for v in combinations(virus,m): # virus의 요소들로 m개만큼 만듦
    ans = min(ans, bfs(v))
if ans != INF:
    print(ans)
else:
    print(-1)
