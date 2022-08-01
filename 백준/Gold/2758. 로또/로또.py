import sys
input = sys.stdin.readline
dp = [[1]*2001 if i == 0 else [0]*2001 for i in range(11)]
for i in range(1, 11):
    for j in range(1, 2001):
        #  j-1 이하의 i개 수를 만드는 방법(j를 사용하지 않고 i개 수를 만드는 방법)
        # + j//2 이하의 i-1개 수를 만드는 방법(j를 사용하여 i개 수를 만드는 방법)
        dp[i][j] = dp[i][j-1]+dp[i-1][j//2]
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(dp[n][m])