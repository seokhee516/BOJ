import sys
from collections import defaultdict
input = sys.stdin.readline
u, n = map(int, input().split())

dd = defaultdict(list)
for _ in range(n):
    name, price = input().split()
    price = int(price)
    dd[price].append(name)

dd = sorted(dd.items(), key=lambda x : (len(x[1]), x[0]))
print(dd[0][1][0], dd[0][0])