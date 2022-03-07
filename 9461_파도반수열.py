import sys
input = sys.stdin.readline

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 101
# 1,2,3 수는 1
d[1] = d[2] = d[3] = 1
# 4,5 수는 2
d[4] = d[5] = 2
T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(6, n+1):
        # i는 이전 수 더하기 5번 전에 수
        d[i] = d[i-1] + d[i-5]
    print(d[n])