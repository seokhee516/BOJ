import sys
N, X = map(int, sys.stdin.readline().split(' '))
A = list(map(int, sys.stdin.readline().split(' ')))
B =[]
for i in range(N):
    if A[i] < X:
        B.append(A[i])
print(' '.join(map(str,B)))