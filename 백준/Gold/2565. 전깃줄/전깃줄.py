import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
# 앞 전봇대 순으로 정렬
data = sorted(data, key = lambda x: x[0])
# print(data)

# DP 테이블 초기화
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[j][1] < data[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)
# max(dp)는 연결될 수 있는 최대 전깃줄
# n - max(dp)는 없애야 하는 전깃줄의 최소 개수
print(n - max(dp))