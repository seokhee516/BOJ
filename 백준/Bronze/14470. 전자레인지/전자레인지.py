import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a > 0:
    print((b-a)*e)
else:
    print(-a*c+d+b*e)