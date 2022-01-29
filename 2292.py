import sys
N = int(sys.stdin.readline().strip())
i = 1
while True:
    room = 1 + 3*i*(i-1)
    if N <= room:
        break
    i += 1
print(i)