import sys
input = sys.stdin.readline
n = int(input())
s = [0 for i in range(301)]
dp = [0 for _ in range(301)]
for i in range(n):
    s[i] = int(input())
# 첫번째 계단
dp[0] = s[0]
# 두번째 계단 무조건 두개
dp[1] = s[0] + s[1]
# 세번째 계단 max(두번째+세번째, 첫번째+세번째)
dp[2] = max(s[1]+s[2], s[0]+s[2])
for i in range(3,n):
    # max(직전칸에서 올라온 경우(현재+직전+전전전),전전칸에서 올라온 경우(현재+전전))
    dp[i] = max(s[i]+s[i-1]+dp[i-3], s[i]+dp[i-2])
print(dp[n-1])