import sys
x, y, w, h = map(int, sys.stdin.readline().split(' '))
i = 0
j = 0
if x > y:
    i = y
else:
    i = x
if (h-y) > (w - x):
    j = (w - x)
else:
    j = (h-y)
if i > j:
    print(j)
else:
    print(i)