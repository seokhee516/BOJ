from functools import cmp_to_key # cmp_to_key가 필요한 경우 import
import sys
input = sys.stdin.readline
N = int(input())
test = list(map(str, input().split()))

# 문자열 자리를 바꿔 크기를 비교하는 함수
def comp(a, b):
    if int(a+b) >= int(b+a): # 큰 것부터 앞으로 가게 정렬  
        return -1
    else:
        return 1
test = sorted(test, key=cmp_to_key(comp)) # 커스텀한 기준으로 sort() 하기
answer = "".join(test) # 문자열로 만들기
print(str(int(answer)))