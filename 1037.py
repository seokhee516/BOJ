import sys
count = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split(' '))))
N = A[0] * A[-1]
print(N)