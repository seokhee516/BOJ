import sys
input = sys.stdin.readline

n, m = map(int, input().split())
site = {}
for _ in range(n):
    a, p  = input().split()
    site[a] = p
for _ in range(m):
    a = input().strip()
    print(site[a])
