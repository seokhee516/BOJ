import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split(' ')))
B, C = map(int, sys.stdin.readline().strip().split(' '))
ans = 0
for i in range(N):
    if A[i] > B:
        A[i] -= B
        ans += 1
        ans += A[i] // C
        if A[i] % C !=0:
            ans +=1
    else:
        ans += 1
print(ans)