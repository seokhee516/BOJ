from collections import deque
import sys
N, M = map(int, input().split())
graph = [[] for _ in range(100001)]
graph[N] = [N-1, N+1, N*2]
distance = [-1] * 100001
distance[N] = 0
q = deque([N])
while q:
    now = q.popleft()
    if now == M:
        print(distance[M])
        break
    for next_node in graph[now]:
        if (next_node < 0) or (next_node > 100000):
            continue
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            graph[next_node]= [next_node-1, next_node+1, next_node*2]