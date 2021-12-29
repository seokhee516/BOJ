import itertools
import sys
N, M = map(int, sys.stdin.readline().split(' '))
arr = list(range(1,N+1))
for r in itertools.permutations(arr, M):
    for i in range(len(r)):
        print(r[i], end = ' ')
    print('')