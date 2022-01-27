import sys
import math
for _ in range(int(sys.stdin.readline().strip())):
    N, M = map(int, sys.stdin.readline().strip().split())
    print(int(math.factorial(M) / (math.factorial(M-N)*math.factorial(N))))