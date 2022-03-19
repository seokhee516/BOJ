import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
if n>=2:
    dp[1] = max(dp[0] + arr[1], arr[1])

for i in range(1,n):
    if dp[i-1] + arr[i] > arr[i]:
        dp[i] = dp[i-1] + arr[i]
    else:
        dp[i] = arr[i]
print(max(dp))