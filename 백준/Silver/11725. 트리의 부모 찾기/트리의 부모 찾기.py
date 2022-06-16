import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
result = [0] * (n+1)
visited = [False] * (n+1)
for _ in range(n-1):
    x, y = map(int, input().strip().split())
    tree[x].append(y)
    tree[y].append(x)
# 트리에 넣기
# print(tree)
# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

# bfs로 트리 탐색
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                # 마지막에 방문하는 노드 담김
                # result[자식] = 부모
                result[i] = v 

bfs(tree, 1, visited)
for i in range(2, n+1):
    print(result[i])