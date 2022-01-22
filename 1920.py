'''
선형 탐색 시간초과

import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
M_num = list(map(int, sys.stdin.readline().strip().split()))
for i in M_num:
    if i in A:
        print(1)
    else:
        print(0)
'''
import sys

def binary_search(element, lst):
    s = 0
    e = len(lst) - 1
    while s <= e:
        m = (s+e) // 2
        if element == lst[m]:
            return print(1)
        elif element < lst[m]:
            e = m - 1
        elif element > lst[m]:
            s = m + 1
    return print(0)

N = int(sys.stdin.readline().strip())
A = sorted(list(map(int, sys.stdin.readline().strip().split())))
M = int(sys.stdin.readline().strip())
M_num = list(map(int, sys.stdin.readline().strip().split()))

for num in M_num:
    binary_search(num, A)
