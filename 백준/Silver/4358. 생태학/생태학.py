import sys
from collections import defaultdict
input = sys.stdin.readline
d = defaultdict(int)
n = 0
while True:
    s = input().strip()
    if not s:
        break
    d[s] += 1
    n += 1
d = sorted(d.items(), key=lambda x: x[0])
for k, v in d:
    print(f'{k} {v/n*100:.4f}')