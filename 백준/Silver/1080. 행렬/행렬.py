import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(n)]
B = [list(map(int, input().strip())) for _ in range(n)]

def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

cnt = 0
if (n<3 or m<3) and A!=B:
    cnt = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if A[i][j] != B[i][j]:
                flip(i, j)
                cnt += 1
            if A == B:
                break
if cnt != -1:
    if A != B:
        cnt = -1
print(cnt)