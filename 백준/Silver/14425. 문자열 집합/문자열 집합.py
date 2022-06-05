import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set()
a = 0
for _ in range(n):
    s.add(input().strip())
for _ in range(m):
    if input().strip() in s:
        a += 1
print(a)