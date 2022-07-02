import sys
input = sys.stdin.readline
n = int(input())
card = [0]
card += list(map(int, input().split()))
dp = [0] * 10001

for i in range(1,n+1):
    dp[i] = card[i] # 카드 한개로 만들 수 있는 수
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[j]+dp[i-j]) # 카드 조합으로 만들 수 있는 수

print(dp[n])