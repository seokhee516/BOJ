import sys
input = sys.stdin.readline

import heapq
import copy

K, N = map(int, input().split())
p_lst = list(map(int, input().split()))
lst, ck = copy.deepcopy(p_lst), set()

heapq.heapify(lst)
idx = 0

while idx < N:
    mn = heapq.heappop(lst)
    if mn in ck:
        continue
    idx += 1
    ck.add(mn)
    for p in p_lst:
        heapq.heappush(lst,mn*p)

print(mn)