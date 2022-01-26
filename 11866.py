from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())

queue = deque()
answer = []
for i in range(1, N+1):
    queue.append(i)
while queue:
    for i in range(K-1): ## 이부분이 포인트!!!
        queue.append(queue.popleft())
    answer.append(queue.popleft())
print("<"+", ".join(map(str, answer))+">")