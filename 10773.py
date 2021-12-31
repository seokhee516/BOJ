import sys
K = int(sys.stdin.readline())
stack = []
for _ in range(K):
    A = int(sys.stdin.readline().strip())
    if A == 0:
        stack.pop()
    else:
        stack.append(A)
print(sum(stack))