import sys
N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
num = sorted(num)
for i in range(N):
    print(num[i])