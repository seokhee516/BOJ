import sys
N = int(sys.stdin.readline())
for _ in range(N):
    case = list(map(str, sys.stdin.readline().strip().split('X')))
    ans = 0
    for c in range(len(case)):
        n = len(case[c])
        ans += n * (n+1)//2
    print(ans)
