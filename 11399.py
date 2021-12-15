import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split(' ')))
P.sort()
ans = time = 0
for i in P:
    time += i
    ans += time
print(ans)