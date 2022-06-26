import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

dp = [[0]*n for i in range(n)] # dp[i][j]는 해당 위치를 방문할 수 있는 횟수
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1: # 마지막 칸에서 중지
            break
        down = i +  graph[i][j]
        right = j + graph[i][j]

        if down < n: # n을 벗어나지 않아 방문 가능하다면
            dp[down][j] += dp[i][j] # 횟수 추가
        if right < n:
            dp[i][right] += dp[i][j]
print(dp[n-1][n-1])
