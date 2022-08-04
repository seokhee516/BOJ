import sys
input = sys.stdin.readline

n = int(input())
ans = [0,0,0]
while n > 0:
    if n >= (60*5):
        n -= (60*5)
        ans[0] += 1
    elif n >= 60:
        n -= 60
        ans[1] += 1
    else:
        n -= 10
        ans[2] += 1
if n != 0:
    print(-1)
else:
    print(*ans)