import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split())) # 잉크지수
B = list(map(int, input().split())) # 점도지수
ans = []
for i in range(n):
    s = 0
    e = n-1
    res = 0
    while s <= e:
        m = (s + e) // 2
        if res == m:
            break
        elif A[i] < B[m]:
            e = m - 1
        else:
            s = m + 1
            res = m
    ans.append(res-i)
print(*ans)