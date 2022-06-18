import sys
input = sys.stdin.readline
'''
점화식
an = a(n-1) + r(n-2) (if n == 3, an += 1)
'''
dp = [0] * 10001
for i in range(4):
    dp[i] = i
for i in range(4,10001):
    dp[i] = dp[i-1] + (dp[i-2] - dp[i-3]) # a(n-2) - a(n-3) = r(n-2)
    if i % 3 == 0:
        dp[i] += 1
    
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])