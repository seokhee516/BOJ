import sys
from collections import deque
from itertools import groupby
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
s = input().strip()
answer = 0

length = [(k,len(list(g))) for k, g in groupby(s)]
i = 0
while i < len(length):
    j = i+1
    d = defaultdict(int)
    d[length[i][0]] += length[i][1]
    while j < len(length):
        d[length[j][0]] += length[j][1]
        if len(d) > n:
            del(d[length[j][0]])
            break
        j += 1
    answer = max(answer, sum(d.values()))
    i += 1
print(answer)