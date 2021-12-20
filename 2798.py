import sys
import itertools
N, M = map(int, sys.stdin.readline().split(' '))
black = list(map(int, sys.stdin.readline().split(' ')))

black_combi = list(map(list, itertools.combinations(black, 3)))
black_sum = []
for b in black_combi:
    if sum(b) <= M:
        black_sum.append(sum(b))
print(max(black_sum))
