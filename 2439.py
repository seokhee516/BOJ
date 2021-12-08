import sys
N = int(sys.stdin.readline())
for i in range(N):
    print(str("*"*(i+1)).rjust(N))