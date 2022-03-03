'''
예제 입력
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

예제 출력 
45
'''
import sys
input = sys.stdin.readline
n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        '''
        # dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
        print(i+1,"일", "p[i]",p[i], "dp[time]", dp[time], "time", time)
        5 일 p[i] 15 dp[time] 0 time 6  - 6번째 날(7일)부터 마지막 날까지 낼 수 있는 최대 이익 0
        4 일 p[i] 20 dp[time] 15 time 4
        3 일 p[i] 10 dp[time] 35 time 3 - 4일부터 마지막 날까지 최대이익 35 i = 2, max_value = 45
        2 일 p[i] 20 dp[time] 0 time 6
        1 일 p[i] 10 dp[time] 35 time 3 - i = 0, max_value = 45
        '''
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    
print(max_value)
'''
print(dp)
[45, 45, 45, 35, 15, 0, 0, 0]
'''