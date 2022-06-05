import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = sum(lst[0:k])
s = ans
for i in range(0,n-k):
    s -= lst[i]
    s += lst[i+k]
    if ans <= s:
        ans = s
print(ans)
