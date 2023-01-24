

import sys
import collections
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
	a,b = map(int,input().split())
	graph[b].append(a)

def bfs(start):
    cnt = 1
    q = collections.deque([start])
    visit = [False] * (n+1)
    visit[start] = True
    
    while q:
        cur = q.popleft()
        cnt += 1
        for v in graph[cur]:
            if not visit[v]:
                visit[v] = True
                q.append(v)
    return cnt
max_cnt = 1
result = []
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        result = [i]
    elif cnt == max_cnt:
        result.append(i)
        
print(*result)
'''
input 
5 4
3 1
3 2
4 3
5 3

해킹 가능
1 -> 3 -> 4, 5
2 -> 3 -> 4, 5

graph 
[[], [3], [3], [4, 5], [], []]
'''