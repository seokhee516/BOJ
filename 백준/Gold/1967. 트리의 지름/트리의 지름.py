# bfs를 두번 사용하여 구현
# 트리에서 아무 노드나 잡고(루트노드) 그 노드에 대한 가장 먼 노드를 구하고 이 노드를 n1이라고 하자.
# n1 에대한 가장 먼 노드를 한번 더 구한다. 이 노드를 n2라고 하자.
# 이제 n1과 n2의 거리가 트리의 지름이 된다.
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, dist = map(int, input().split())
    tree[a].append((b,dist))
    tree[b].append((a,dist))
# print(tree) [[], [(2, 3), (3, 2)], [(1, 3), (4, 5)], [(1, 2), (5, 11), (6, 9)], [(2, 5), (7, 1), (8, 7)], [(3, 11), (9, 15), (10, 4)], [(3, 9), (11, 6), (12, 10)], [(4, 1)], [(4, 7)], [(5, 15)], [(5, 4)], [(6, 6)], [(6, 10)]]  

def bfs(v): # 노드 v에서 최대 거리
    q = deque([(v, 0)])
    visited = [False] * (n+1)
    visited[v] = True # 시작 노드 방문 표시

    max_node = [0,0] # 가장 먼 노드 [노드번호, 최대 거리]
    while q:
        now, now_dist = q.popleft()
        for child, child_dist in tree[now]:
            if not visited[child]: # 자식 노드 방문하지 않았다면
                visited[child] = True # 방문 후
                q.append((child, now_dist+child_dist)) # 현재 거리 + 자식 거리
                if max_node[1] < now_dist+child_dist: # 더 거리가 먼 경우 업데이트
                    max_node[0] = child
                    max_node[1] = now_dist+child_dist
    return max_node

n1 = bfs(1) # 루트 노드에서 가장 먼 노드
# print(n1) [9, 28]
n2 = bfs(n1[0]) # n1에서 가장 먼 노드
# print(n2) [12, 45]
print(n2[1]) # n1에서 n2의 거리