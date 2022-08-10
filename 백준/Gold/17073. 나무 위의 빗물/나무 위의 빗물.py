import sys
input = sys.stdin.readline
from collections import deque
# 물의 양은 그대로 w로 고정이고, 물이 움직이지 않은 상태는 모든 물이 leaf 노드에 들어갔다는 의미이므로 leaf 노드의 개수를 구해서 w/(leaf노드 개수)
n,w= map(int, input().split())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 트리의 부모찾기
result = [0] * (n+1)
visited = [False] * (n+1)
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]: # 마지막에 방문하는 노드 담김
                q.append(i)
                visited[i] = True
                # result[자식] = 부모
                result[i] = v 

bfs(tree, 1, visited)
# 전체 노드 수 - 부모 노드 수 = leaf 노드 수
print(w/(n-len(set(result[2:]))))
