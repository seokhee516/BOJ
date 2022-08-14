import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split())) # 잉크지수
B = list(map(int, input().split())) # 점도지수
ans = []
for i in range(n): # 잉크지수 하나씩 확인
    s = i
    e = n-1
    res = 0
    while s <= e:
        m = (s + e) // 2
        if A[i] < B[m]: # 점도지수가 잉크지수보다 크다면
            e = m - 1 # 더 작은 범위 확인
        else: # 점도지수가 잉크지수보다 작거나 같다면
            s = m + 1 # 더 큰 범위 확인
            res = m # 결과값 업데이트
    ans.append(res-i) # 현재 위치부터 점도지수가 잉크지수보다 작거나 같은 칸까지 개수
print(*ans)