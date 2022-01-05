'''
유클리드 호제법
a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
a = 72
b = 30
r = a % b
r_ = b % r
if r % r_ ==0:
    gcd = r_
lcm = a*b / r_
'''

import sys

def GCD(A,B):
    if A % B ==0:
        return B
    else:
        return GCD(B,A%B)


T = int(sys.stdin.readline())
for _ in range(T):
    B, A = map(int, sys.stdin.readline().strip().split(' '))
    LCM = int(A*B / GCD(A,B))
    print(LCM)