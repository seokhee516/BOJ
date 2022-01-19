import sys
T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().strip().split(' '))
    if N%H ==0:
        room = str(H) + str(N//H).rjust(2,"0")
    else:
        room = str(N%H) + str(N//H+1).rjust(2,"0")
    print(int(room))

