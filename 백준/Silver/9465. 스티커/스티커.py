import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n >= 2:
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]

        for i in range(2,n):
            dp[0][i] += (max(max(dp[0][i-2:i-1]), max(dp[1][i-2:i])) + sticker[0][i])
            dp[1][i] += (max(max(dp[1][i-2:i-1]), max(dp[0][i-2:i])) + sticker[1][i])

    print(max(max(dp[0]),max(dp[1])))