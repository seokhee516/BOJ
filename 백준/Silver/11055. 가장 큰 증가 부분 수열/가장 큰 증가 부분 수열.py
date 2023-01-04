import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

dp=array[:] # 수열 전체 dp에 복사
for i in range(n):
  for j in range(i):
    if array[j]<array[i]: # 증가하는 수열이라면
        dp[i]=max(dp[i], dp[j]+array[i]) # 현재값, 증가하는 수열 더한 값
print(max(dp))

'''
10
1 100 2 50 60 3 5 6 7 8
dp = [1, 101, 3, 53, 113, 6, 11, 17, 24, 32]
'''