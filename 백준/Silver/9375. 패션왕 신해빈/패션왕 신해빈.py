import sys
from collections import Counter
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = []
    for j in range(n):
        a, b = input().split()
        # 의상의 종류만 저장
        s.append(b)
    c_list = Counter(s).values()
    res = 1 # 경우의 수 저장할 값
    for c in c_list:
        # 의상의 종류 +1 곱해줌
        res *= c+1
    # 모두 안입는 경우 제외
    res -=1
    print(res)

'''
hat headgear
sunglasses eyewear
turban headgear
예를 들어 위 케이스는
(hat), (turban), (sunglasses), (hat,sunglasses), (turban,sunglasses)로 총 5가지이다. 
이는 headgear, eyewear 각각 종류를 입는 경우와 안입는 경우로 나눌 수 있다.

eyewear(sunglasses) 입는 경우
(hat,sunglasses), (turban,sunglasses), (sunglasses)
eyewear(sunglasses) 안 입는 경우
(hat, x), (turban, x), (x, x)
즉 종류의 수에 1을 더해  경우를 입는 경우와 안입는 경우를 나눠준 후 각각 곱해준다.
그리고 마지막에 모두 안입는 경우를 빼서 알몸이 아닌 상태를 제외해준다. 
'''