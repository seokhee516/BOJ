import sys
input = sys.stdin.readline
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

n, m = map(int, input().split())
print(n+m-gcd(n,m))