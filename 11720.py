import sys
N = int(sys.stdin.readline())
X = sys.stdin.readline()
ans = 0
for i in range(N):
    ans += int(X[i])
print(ans)