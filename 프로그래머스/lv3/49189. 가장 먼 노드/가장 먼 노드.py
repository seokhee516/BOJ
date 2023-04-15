from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visited[1] = 1
    q = deque([1])
    
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)
    max_v = max(visited)
    answer = visited.count(max_v)
    
    return answer