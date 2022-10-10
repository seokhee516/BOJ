import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

dist = [0] * (n+1)
def bfs(start):
    q = deque([start])
    while q:
        v = q.popleft()
        for i in tree[v]:
            if i != start and dist[i] == 0:
                q.append(i)
                dist[i] = dist[v] + 1
bfs(a)
if dist[b] == 0:
    print(-1)
else:
    print(dist[b])