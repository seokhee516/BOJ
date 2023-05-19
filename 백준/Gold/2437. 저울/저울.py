N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 0

for i in A:
    if i <= ans + 1:
        ans += i
    else:
        break
print(ans+1)