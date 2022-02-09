'''
DFS 알고리즘
시작 노드를 옅은 회색 표시 후, 스택에 넣음
스택에 아무 노드가 없을 때까지:
    스택  가장 위 노드를 꺼낸다
    노드를 방문 (진한회색)표시한다
    인접한 노드들을 모두 보면서:
    처음 방문하거나 스택에 없는 노드면:
        옅은 회색 표시를 해준다
        스택에 넣는다.
'''

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# visited = [False] * 9
# dfs(graph, 1, visited)
'''
BFS 알고리즘
시작 노드를 방문 표시 후, 큐에 넣음 
큐에 아무 노드가 없을때까지:
    큐 가장 앞 노드를 꺼낸다
    꺼낸 노드에 인접한 노드들을 모두 보면서:
        처음 방문한 노드면: 
            방문한 노드 표시를 해준다
            큐에 넣어준다
'''
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 9
bfs(graph, 1, visited)