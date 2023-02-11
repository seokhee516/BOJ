import sys
input = sys.stdin.readline

n = int(input()) # 노드의 개수
tree = [[] for _ in range(n)]
node = list(map(int, input().split())) #  0번 노드부터 N-1번 노드까지, 각 노드의 부모
k = int(input()) # 지울 노드의 번호
cnt = 0

def dfs(k, node):
    node[k] = -2 # 노드 삭제
    for i in range(len(node)):
        if k == node[i]: # 삭제한 노드가 부모 노드라면
            dfs(i, node) # 자식 노드도 삭제

dfs(k, node)
for i in range(len(node)):
    if node[i] != -2 and i not in node: # 삭제한 노드가 아니고, 부모 노드가 아니라면
        cnt += 1

print(cnt)
