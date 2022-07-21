import sys
input = sys.stdin.readline
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
# for _ in range(n):
#     arr.append(list(map(int, input().split())))
lst = [tuple(map(int, input().split())) for _ in range(k)]

from itertools import permutations
import copy
# print(list(permutations(lst,k)))
answer = 1e9
# rotate(r-s-1, c-s-1, r+s-1, c+s-1, arr)
permutations = list(permutations(lst,k))
for permutation in permutations:
    arr_copy = copy.deepcopy(arr)
    for p in permutation:
        r, c, s = p
        # print(r-s-1, c-s-1, r+s-1, c+s-1)
        for i in range((2*s+1)//2):
            # print("i",i)
            rotate(r-s-1+i, c-s-1+i, r+s-1-i, c+s-1-i, arr_copy)
        # print(arr_copy)
    # print("arr_copy",arr_copy)
    # print()
    for i in range(n):
        # print(arr_copy[i])
        answer = min(answer, sum(arr_copy[i]))
print(answer)