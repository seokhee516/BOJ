import sys
input = sys.stdin.readline
'''
처음에 이렇게 풀었는데 왜 틀렸는지 모르겠당...ㅠ.ㅠ
N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

# 체력 0, 기쁨 0 시작
cache = {0:0}
for i in range(N):
    temp = {}
    for l, j in cache.items(): # 체력은 최소 기쁨은 최대로 저장
        if l + L[i] < 100 and (j + J[i]) > cache.get(l + L[0], 0): # 현재 체력에서 다음 체력을 더했을 때 100보다 작고, 현재 기쁨과 다음 기쁨이 같은 값의 체력이 저장된 기쁨보다 크면 저장
            temp[l + L[i]] = j + J[i]
    # 캐시에 저장
    cache.update(temp)

print(max(cache.values()))
'''
N = int(input()) 
L = [0] + list(map(int, input().split()))
P = [0] + list(map(int, input().split()))
dp = [[0] * 101 for _ in range(N+1)] 

for i in range(1, N+1): 
    for j in range(1, 101): 
        if L[i] <= j: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + P[i]) 
        else: 
            dp[i][j] = dp[i-1][j] 

print(dp[N][99]) 
# 왜 99일까??? 
# 체력이 1이 기준이며, 출력할 때 dp[n][100]을 출력하면 세준이가 인사를 하다 죽어버린 경우이니 오답이다. dp[n][99]를 출력한다.
# 라고 하는데 이해가 안된다잉