import sys
input = sys.stdin.readline
n, s, m = map(int, input().split())
V = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(1, n+1): # 곡의 개수 만큼
    for P in range(m+1): # 0 ~ 최대 볼륨 확인 & 볼륨 조절 가능에 1 표시
        if dp[i-1][P] == 1: # 이전 곡에서 볼륨 조절 가능하면
            if 0 <= P+V[i-1] <= m: # 볼륨 증가
                dp[i][P+V[i-1]] = 1 
            if 0 <= P-V[i-1] <= m: # 볼륨 감소
                dp[i][P-V[i-1]] = 1

ans = -1
# 볼륨의 최댓값 출력하기 위해 내림차순 반복문 실행
for i in range(m, -1, -1):
    if dp[n][i] ==  1: # 마지막 곡에서 내림차순으로 처음 1이 최댓값
        ans = i # 인덱스 i는 조절 가능한 볼륨 값 
        break
print(ans)

'''
input
3 5 10
5 3 7

dp
[[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
'''