from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
ck = [0] *(n+1)
ck[1] = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s=1):
    q = deque([s])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if ck[nx] == 0:
                ck[nx] = ck[x] + 1
                q.append(nx)

bfs()
res = ck.count(2) + ck.count(3)
print(res)