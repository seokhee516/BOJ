import sys
H, M = map(int, sys.stdin.readline().split(' '))
if M < 45:
    H -=1
    M = (15 + M)
    if H == -1:
        H = 23
else:
    M = (M - 45)
print(H, M)