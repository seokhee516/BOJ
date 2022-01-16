import sys
import math
N, K = map(int, sys.stdin.readline().strip().split(' '))
if K < 0:
    answer = 0
elif K > N:
    answer = 0
else:
    answer = math.factorial(N) / (math.factorial(K) * math.factorial(N-K))
print(int(answer))