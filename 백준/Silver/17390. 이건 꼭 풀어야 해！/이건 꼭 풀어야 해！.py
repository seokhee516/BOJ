import sys
input = sys.stdin.readline
n,q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A.insert(0,0)
for i in range(1,n+1):
    A[i] = A[i] + A[i-1]
# print(A) [0, 1, 3, 6, 10, 15]
for _ in range(q):
    l, r = map(int,input().split())
    print(A[r]-A[l-1])