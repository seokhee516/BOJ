# 규칙을 찾기가 어려웠던 문제
# 2차원 dp를 사용하는 방법!!!
import sys
input = sys.stdin.readline
n = int(input()) # n은 1보다 크거나 같고 100보다 작거나 같은 자연수
dp = [[0 for i in range(10)] for j in range(101)] # 가로 10개 세로 100개 짜리
for i in range(1,10):
    dp[1][i] = 1
# dp[1] -> [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] i길이의 j로 끝나는 수의 개수
# dp[2] -> [1, 1, 2, 2, 2, 2, 2, 2, 2, 1]
for i in range(2, n+1):
    for j in range(10):
        if j == 0: # 끝자리가 0일때 
            dp[i][j] = dp[i - 1][1] # 그 전 길이의 1자리에서만 만들 수 있음 ex) 1 -> 10
        elif j == 9: # 끝자리가 9일때 
            dp[i][j] = dp[i - 1][8] # 그 전 길이의 8자리에서만 만들 수 있음 ex) 8 -> 89
        else: # 그 외 숫자
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] # 앞자리에서 + 뒷자리에서 만들기
# n 길이의 계단 수 합 , 조건에 따라 나눈 나머지 출력
print(sum(dp[n]) % 1000000000)