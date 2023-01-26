import sys
from collections import deque
input = sys.stdin.readline
c = int(input())
for _ in range(c):
    test = list(input().strip())
    st1 = deque([])
    st2 = deque([])
    for t in test:
        if t == '<':
            if not st1:
                continue
            st2.appendleft(st1.pop())
        elif t == '>':
            if not st2:
                continue
            st1.append(st2.popleft())
        elif t == '-':
            if not st1:
                continue
            st1.pop()
        else:
            st1.append(t)
    st1.extend(st2)
    print(''.join(st1))