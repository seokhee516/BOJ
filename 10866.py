import sys
N = int(sys.stdin.readline())

from collections import deque
deque = deque()
for _ in range(N):
    A = sys.stdin.readline().strip().split(' ')
    if A[0] =='push_front':
        deque.appendleft(A[1])
    elif A[0] =='push_back':
        deque.append(A[1])
    elif A[0] =='pop_front':
        try:
            if len(deque) != 0:
                print(deque.popleft())
            else:
                print(-1)
        except:
            print(-1)
    elif A[0] =='pop_back':
        try:
            if len(deque) != 0:
                print(deque.pop())
            else:
                print(-1)
        except:
            print(-1)
    elif A[0] =='size':
        print(len(deque))
    elif A[0] =='empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif A[0] =='front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif A[0] =='back':
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)