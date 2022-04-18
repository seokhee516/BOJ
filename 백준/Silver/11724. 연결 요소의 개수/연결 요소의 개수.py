import sys
input = sys.stdin.readline

# 정점의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 메서드 정의
def dfs(graph,v,visited):
    # 현재 노드 방문처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0 # 연결된 요소의 개수
visited = [False] * (n+1)
for i in range(1,n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        cnt += 1 # 처음 방문할때만 카운트
print(cnt)