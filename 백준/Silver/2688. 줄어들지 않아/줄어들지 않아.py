import sys
n = 64
dp = [[0 for i in range(10)] for j in range(65)]
for i in range(10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

t = int(input())
for _ in range(t):
    k = int(input())
    print(sum(dp[k]))