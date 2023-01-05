import sys
input = sys.stdin.readline
n = int(input())
dp = [[0] * 3 for _ in range(n+1)] 
for i in range(3):
    dp[1][i] = 1
for i in range(2, n+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901
print(sum(dp[n])%9901)

'''
line 4 input 3일때 dp: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] 
line 5~6 input 3일때 dp: [[0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]] 
line 7~9
dp[i][0] : i번째 행에 사자를 왼쪽 배치. i-1번째 행에 사자가 오른쪽에 있거나(dp[i-1][1]) 없는(dp[i-1][2]) 경우
dp[i][1] : i번째 행에 사자를 오른쪽 배치. i-1번째 행에 사자가 왼쪽에 있거나(dp[i-1][0]) 없는(dp[i-1][2]) 경우
dp[i][2] : i번째 행에 사자 없음. i-1번째에 어느 위치에 사자가 있어도 상관없음 (dp[i-1][0], dp[i-1][1], dp[i-1][2])
line 11
input 3일때 dp: [[0, 0, 0], [1, 1, 1], [2, 2, 3], [5, 5, 7]]
dp[n]: [5, 5, 7] sum(dp[n]): 17
'''