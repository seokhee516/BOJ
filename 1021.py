import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
queue = deque(range(1, N+1))
num = list(map(int, sys.stdin.readline().strip().split()))

ans = 0
for n in num:
    left = 0
    right = 0
    for i in queue:
        if i == n:
            break
        left += 1
    for j in range(len(queue)-1,0,-1):
        right += 1
        if queue[j] == n:
            break
    if left < right:
        ans += left
        for _ in range(left):
            queue.append(queue.popleft())
        queue.popleft()
    else:
        ans += right
        for _ in range(right):
            queue.insert(0,queue.pop())
        queue.popleft()
print(ans)