from functools import cmp_to_key # cmp_to_key가 필요한 경우 import
'''
2 4
7
4
7774 앞

3 4
1
10
100
110100100 뒤

3 4
9
910
901
9910910901 가운데
'''
import sys
input = sys.stdin.readline
K, N = map(int, input().split())
test = [input().strip() for _ in range(K)]

# 문자열 자리를 바꿔 크기를 비교하는 함수
def comp(a, b):
    if int(a+b) >= int(b+a): # 큰 것부터 앞으로 가게 정렬  
        return -1
    else:
        return 1
test = sorted(test, key=cmp_to_key(comp)) # 커스텀한 기준으로 sort() 하기
idx = test.index(str(max(map(int, test)))) # 가장 큰 수 인덱스 찾기 앞, 뒤, 중간 올 수 있음
test[idx] *= (N-K+1) # 가장 큰 수 여러번 곱해주기
answer = "".join(test) # 문자열로 만들기
print(answer)

