import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
def con_mul(a, b):
    if b == 1:
        return a % c
    elif b == 2:
        return a**2 % c
    else:
        if b % 2 == 0:
            return (con_mul(a, b//2)**2) % c
        else:
            return (con_mul(a, b//2)**2)*a % c

print(con_mul(a, b))