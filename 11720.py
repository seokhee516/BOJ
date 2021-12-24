import sys
N = int(sys.stdin.readline())
X = sys.stdin.readline()
# print(X)
# X = '10987654321'
ans = 0
for i in range(N):
    ans += int(X[i])
print(ans)