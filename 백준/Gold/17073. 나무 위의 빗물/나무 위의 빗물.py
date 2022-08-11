import sys
input = sys.stdin.readline
# 물의 양은 그대로 w로 고정이고, 물이 움직이지 않은 상태는 모든 물이 leaf 노드에 들어갔다는 의미이므로 leaf 노드의 개수를 구해서 w/(leaf노드 개수)
n,w= map(int, input().split())
tree = [0] * (n+1)
for i in range(n-1):
    u, v = map(int, input().split())
    tree[u] += 1
    tree[v] += 1
# 연결된 간선이 하나이면 leaf 노드이다.
cnt = 0
for i in range(2,n+1): # root 노드는 제외해준다.
    if tree[i] == 1:
        cnt += 1
print(w/cnt)