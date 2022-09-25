import sys
input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()
# 2차원 배열을 사용한 동적 계획법
h, w = len(s1), len(s2)
dp = [[0]*(w+1)for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        
        if s1[i-1] == s2[j-1]: # 같은 알파벳인 경우
            dp[i][j] = dp[i-1][j-1] + 1 # 글자를 추가하기 전의 LSC값보다 1 더해서 저장
        else: # 다른 경우
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) # 이전까지 비교한 값중 최대값
'''
dp
[[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 2, 2, 2], 
[0, 1, 2, 2, 2, 3, 3], 
[0, 1, 2, 2, 2, 3, 3], 
[0, 1, 2, 2, 2, 3, 4], 
[0, 1, 2, 3, 3, 3, 4]]
'''
print(dp[-1][-1])