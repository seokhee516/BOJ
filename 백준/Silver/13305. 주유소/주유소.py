N = int(input())
L = list(map(int, input().split()))
C = list(map(int, input().split()))
j = 0
ans = 0
for i in range(len(L)):
    if C[j] >= C[i]:
        j=i
    ans += L[i] * C[j]
print(ans)