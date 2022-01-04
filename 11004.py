import sys
N, K = map(int, sys.stdin.readline().strip().split(' '))
A = list(map(int, sys.stdin.readline().split(' ')))
print(sorted(A)[K-1])
