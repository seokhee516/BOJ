import sys
from collections import deque
N = 4
i = 0
A = list(map(int, sys.stdin.readline().strip().split()))
B = deque([(A[i], i) for i in range(len(A))])
print(B)