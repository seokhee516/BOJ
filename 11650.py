import sys
N = int(sys.stdin.readline())
a = []
for _ in range(N):
    a.append(list(map(int, sys.stdin.readline().split(' '))))
for x, y in sorted(a):
    print(x, y)
