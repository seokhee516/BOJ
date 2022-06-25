import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    s = input().split()
    if s ==['0']:
        break
    k = s[0]
    s = s[1:]
    for lst in list(combinations(s, 6)):
        for l in lst:
            print(l, end =' ')
        print()
    print()