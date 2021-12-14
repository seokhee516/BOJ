import sys
N, K= map(int, sys.stdin.readline().split(' '))
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
result = 0
for i in range(1,N+1):
    if K // A[-i] != 0:
        result += (K // A[-i])
        K = K % A[-i]
print(result)