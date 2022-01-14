import sys
N = int(sys.stdin.readline())

from collections import deque
queue = deque()
for _ in range(N):
    A = sys.stdin.readline().strip().split(' ')
    if A[0] =='push':
        queue.append(A[1])
    elif A[0] =='pop':
        try:
            if len(queue) != 0:
                print(queue.popleft())
            else:
                print(-1)
        except:
            print(-1)
    elif A[0] =='size':
        print(len(queue))
    elif A[0] =='empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif A[0] =='front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif A[0] =='back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)