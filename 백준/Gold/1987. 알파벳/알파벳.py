import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = set() # 시간 절약을 위해 set
ans = 0
def dfs(x,y,cnt):
    global ans
    ans = max(ans, cnt) # 최대값
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<= nx < n) and (0 <= ny < m) and (graph[nx][ny] not in visited): # 다른 알파벳일 때
            visited.add(graph[nx][ny]) # 지나온 알파벳 표시
            dfs(nx,ny,cnt+1)
            visited.remove(graph[nx][ny])
visited.add(graph[0][0]) # 좌측 상단 포함
dfs(0,0,1) # 좌측 상단 포함이므로, cnt = 1

print(ans)