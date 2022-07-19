import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
for _ in range(n):
    a, b = input().strip().split()
    lst.append(b)
combis = []
for i in range(1,n+1):
    for combi in list(combinations(lst, i)):
        s = ["N"] * m
        for j in range(i):
            for k in range(m):
                if combi[j][k] == "Y":
                    s[k] = "Y"
        combis.append((i, s.count("Y")))
answer = sorted(combis, key=lambda x:(x[1],-x[0]), reverse=True)
if answer[0][1] == 0:
    print(-1)
else:
    print(answer[0][0])