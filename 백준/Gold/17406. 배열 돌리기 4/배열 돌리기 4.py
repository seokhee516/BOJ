import sys
from itertools import permutations
import copy
input = sys.stdin.readline
# 시계 방향으로 회전
def rotate(x1, y1, x2, y2, matrix):
    i = x1
    j = y1
    now = matrix[x1][y1]
    for j in range(y1+1, y2+1):
        next = matrix[i][j]
        matrix[i][j] = now
        now = next
    for i in range(x1+1, x2+1):
        next = matrix[i][j]
        matrix[i][j] = now
        now = next
    for j in range(y2-1, y1-1, -1):
        next = matrix[i][j]
        matrix[i][j] = now
        now = next
    for i in range(x2-1, x1-1, -1):
        next = matrix[i][j]
        matrix[i][j] = now
        now = next

n, m, k= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 연산 리스트
lst = [tuple(map(int, input().split())) for _ in range(k)]

answer = 1e9
permutations = list(permutations(lst,k)) # 모든 연산 순열 확인
for permutation in permutations:
    arr_copy = copy.deepcopy(arr) # 딥 카피로 돌려주기
    for p in permutation:
        r, c, s = p
        for i in range((2*s+1)//2): # 한칸씩 돌리기
            rotate(r-s-1+i, c-s-1+i, r+s-1-i, c+s-1-i, arr_copy)
    for i in range(n):
        answer = min(answer, sum(arr_copy[i])) # 배열의 최솟값
print(answer)
