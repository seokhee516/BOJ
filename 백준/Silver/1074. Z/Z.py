import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
ans = 0
def z(n, x, y):
    global ans
    if x == r and y == c:
        print(int(ans))
        return 
    if n == 1: # n이 1일때 한칸씩 옆으로 가는 개념
        ans += 1
        return
    if not (x<=r<x+n and y<=c<y+n): # 찾으려는 값이 범위를 벗어나는 경우
        ans += (n*n)
        return
            
    z(n/2, x, y) # 2로 먼저 나눔
    z(n/2, x, y+n/2) # 오른쪽 먼저 확인
    z(n/2, x+n/2, y) # 아래 확인
    z(n/2, x+n/2, y+n/2) # 오른쪽 아래 확인
z(2**n,0,0)