import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split(' '))))
lst = sorted(lst, key = lambda x: (x[1], x[0]))
for i in lst:
    print(i[0], i[1])