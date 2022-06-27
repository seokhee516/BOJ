import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
# dp = [list(map(int, input().split())) for i in range(n)]

dp = [[0]*m for i in range(n)]
dp[0][0] = graph[0][0]

dx = [1, 0, 1]
dy = [0, 1, 1]

for i in range(n):
    for j in range(m):
        for k in range(3):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < n and ny < m:
                dp[nx][ny] = max(dp[nx][ny],dp[i][j] + graph[nx][ny])

print(dp[n-1][m-1])