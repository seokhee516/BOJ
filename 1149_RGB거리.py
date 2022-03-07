import sys
input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
for i in range(1,n):
    # 0, 1, 2 는 빨강, 초록, 파랑 집 의미
    # 현재 줄의 비용 = 이전 줄의 최소비용(min) + 현재 줄의 비용
    array[i][0] = min(array[i-1][1], array[i-1][2]) + array[i][0]
    array[i][1] = min(array[i-1][0], array[i-1][2]) + array[i][1]
    array[i][2] = min(array[i-1][0], array[i-1][1]) + array[i][2]
print(min(array[n-1][0], array[n-1][1], array[n-1][2]))