from logging import makeLogRecord
import sys
input = sys.stdin.readline
INF = 1e10
n, m = map(int, input().split())
data = list(map(int, input().split()))
left, right = max(data), sum(data)

while left <= right:
    mid = (left+right) // 2
    cnt = 0
    tmp = 0
    for i in range(n):
        if tmp + data[i] > mid: 
            cnt += 1
            tmp = 0
        tmp += data[i]
    if tmp:
        cnt += 1
    else:
        cnt += 0
    if cnt <= m:
        right = mid -1
    else:
        left = mid + 1
print(left)