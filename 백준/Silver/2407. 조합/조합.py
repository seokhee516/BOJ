import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [0] * 101
dp[5] = 120
for i in range(6,n+1):
    dp[i] = dp[i-1] * i
'''
주의할 부분 
 / 로 나누고 int를 붙이게 되면 소수로 변환할때 오차가 생긴다.. 
int 형으로 계산하고 소수만 떼주는 //를 사용해야 한다.
'''
ans = dp[n] // (dp[n-m] * dp[m])
print(ans)

'''
처음에는 이렇게 풀었는데 부동소수점 때문에 값이 구해지지 않았다..
부동소수점이란 컴퓨터가 숫자를 2진수로 표현하기 때문에 어쩔수 없이 생기는 오차이다.
예를들어 0.3과 같은 숫자는 0.01001100110011... 무한반복한다.
이러한 숫자를 처리할때 무한반복 되는 값에서 근사값을 저장하게 되고 여기서 오차가 발생하는 것이다.

그래서 아래 식에서 임의 큰 수의 나눗셈을 할때는 이 부동소수점으로 인해 오차가 발생하게 된다.
따라서 DP를 활용하여 풀 수 있다.

numerator = 1
denominator = 1
for i in range(n, m-1, -1):
    numerator *= i
for j in range(m, 0, -1):
    denominator *= j
answer = int(numerator) // int(denominator)
answer
'''

