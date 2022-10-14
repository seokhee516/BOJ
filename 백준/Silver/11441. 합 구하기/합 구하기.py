import sys
input = sys.stdin.readline

n=int(input())
lst = list(map(int, input().split()))
# i가 1일때를 위해 0 넣기
lst.insert(0,0)
m=int(input())
# 누적합 구하기
for i in range(1,n+1):
    lst[i] = lst[i] + lst[i-1]

for _ in range(m):
    a, b = map(int, input().split())
    print(lst[b] - lst[a-1])