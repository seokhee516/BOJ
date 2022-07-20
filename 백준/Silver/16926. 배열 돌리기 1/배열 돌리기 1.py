import sys
from collections import deque
input = sys.stdin.readline
def rotate(x1, y1, x2, y2, matrix):
    i = x1
    j = y1
    now = matrix[x1][y1]
    for i in range(x1+1, x2):
        next = matrix[i][j]
        matrix[i][j] = now
        now = next
    for j in range(y1+1, y2):
        next = matrix[i][j]
        matrix[i][j] = now
        now = next
    for i in range(x2-2, x1-1, -1):
        next = matrix[i][j]
        matrix[i][j] = now
        now = next
    for j in range(y2-2, y1-1, -1):
        next = matrix[i][j]
        matrix[i][j] = now
        now = next


n, m, r= map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(min(n,m)//2):
    cnt = 0
    while cnt < r:
        rotate(i, i, n-i, m-i, arr)
        cnt += 1
for i in range(n):
    print(*arr[i])