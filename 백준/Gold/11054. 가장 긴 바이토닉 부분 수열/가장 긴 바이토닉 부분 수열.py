import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

dp = [1] * n
r_dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
array.reverse()
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            r_dp[i] = max(r_dp[i], r_dp[j]+1)
r_dp.reverse()
for i in range(n):
    dp[i] += r_dp[i]
print(max(dp)-1)