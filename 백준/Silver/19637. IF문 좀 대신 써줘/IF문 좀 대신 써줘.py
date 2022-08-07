import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
name = []
strength = []
for i in range(n):
    na, st = input().split()
    name.append(na)
    strength.append(int(st))
for j in range(m):
    v = int(input())
    print(name[bisect_left(strength, v)])