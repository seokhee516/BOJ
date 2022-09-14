from collections import deque
# 트리에 연결된 노드의 개수 세기
def bfs(wire, tree, n):
    cnt =0
    visited = [False] * (n+1) 
    visited[wire[0]] = True # 처음 노드 방문표시
    q = deque([wire[0]])
    while q:
        v = q.popleft()
        for i in tree[v]: # 트리 확인
            if not visited[i] and i != wire[1]: # 방문하지 않았고, 끊어지지 않았을 때
                visited[i] = True # 방문
                q.append(i)
                cnt += 1 # 개수 세기
    return cnt

def solution(n, wires):
    ans = 1e9
    # 트리 만들기
    tree = [[] for _ in range(n+1)]
    for x,y in wires:
        tree[x].append(y)
        tree[y].append(x)
    
    # 전선 하나씩 끊어가면서 확인
    for wire in wires:
        tmp = bfs(wire, tree, n)
        ans = min(ans, abs(n-2*(tmp+1))) # 개수의 차이 절대값 가장 적도록
    return ans