import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())

dot = defaultdict(list)
for _ in range(n):
    roc, col = input().split()
    dot[col].append(int(roc))
answer = 0
for k, v in dot.items():
    v.sort()
    answer += v[1]-v[0]
    if len(v) > 2:
        for i in range(1,len(v)-1):
            answer += min(v[i+1]-v[i],v[i]-v[i-1])
    answer += v[-1]-v[-2]
print(answer)
