INF = 1000001
num = [True for i in range(INF)] # 소수(True) 담을 리스트
# 에라토스테네스의 체
for i in range(2, 1001):
    if num[i]:
        for j in range(i+i, INF, i): # 배수 지워나가기
            num[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(2, INF):
        if num[i] and num[n-i]: # i가 작은 수 부터 존재 -> b-a가 가장 큰 것 찾음
            print(n, "=", i, "+", n-i)
            break