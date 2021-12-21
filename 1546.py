import sys
N = int(sys.stdin.readline())
math = list(map(int, sys.stdin.readline().split(' ')))
best_math = max(math)
for i in range(N):
    math[i] = (math[i] / best_math) * 100
print(sum(math)/N)
