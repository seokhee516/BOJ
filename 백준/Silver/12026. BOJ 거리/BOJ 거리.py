import sys
input = sys.stdin.readline
n = int(input())
block = input().strip()

INF = 1e9
dp = [INF] * n
dp[0] = 0
for i in range(1, n):
    now = block[i]
    if now == 'B':
        prev = 'J'
    elif now == 'O':
        prev = 'B'
    elif now == 'J':
        prev = 'O'
    for j in range(i):
        if block[j] == prev:
            dp[i] = min(dp[i], dp[j] + (i-j)**2) # 그 전까지 거리 + 그 전에서 현재까지 거리

if dp[n-1] == INF:
    ans = -1
else:
    ans = dp[n-1]
print(ans)

