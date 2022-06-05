import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
# i가 1일때를 위해 0 넣기
lst.insert(0,0)

# 누적합 구하기
for i in range(1,n+1):
    lst[i] = lst[i] + lst[i-1]

for _ in range(m):
    # i 부터 j 까지 구간 합
    i, j = map(int, input().split())
    # j 까지 누적합 - (i-1) 까지 누적합
    print(lst[j] - lst[i-1])