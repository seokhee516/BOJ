import sys
from collections import deque
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))
    
    A = deque([(A[i], i) for i in range(len(A))])
    cnt = 0

    while len(A) > 0:
        if max(A,key=lambda item:item[0])[0] != A[0][0]:
            A.append(A.popleft())
        else:
            temp = A.popleft()
            cnt += 1
            if temp[1] == M:
                break
    print(cnt)