# 에라토스테네스의 체
def isPrime(a):
    if a<2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    a = n // 2  # 차이가 가장 작은 것 구하기 위해 가운데 값을 구함
    b = n // 2
    for _ in range(n//2): 
        if isPrime(a) and isPrime(b): # a와 b 가 소수라면
            print(a, b) # 출력
            break
        else:
            a -= 1 # 한자리씩 멀어지면서 확인
            b += 1

