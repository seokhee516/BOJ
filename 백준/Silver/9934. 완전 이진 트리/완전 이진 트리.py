k = int(input())
inorder = list(map(int, input().split()))

tree = [[] for _ in range(k)]

def dfs(inorder, depth):
    mid = (len(inorder)//2)             # tree의 root인덱스를 찾아낸다
    tree[depth].append(inorder[mid])    # 해당 깊이에 해당하는 노드를 추가한다
    
    if len(inorder) == 1:               # 노드가 자식을 가지고 있지 않다면 끝
        return
    
    dfs(inorder[:mid], depth+1)         # 왼쪽 자식
    dfs(inorder[mid+1:], depth+1)         # 오른쪽 자식
    
dfs(inorder, 0)

for t in tree:
    print(*t)

'''
문제에서 주어진 방문 순서는 중위 순회이다.
중위순회를 반대로 실행하여 tree를 만들어야 한다.
중위 순회로 입력된 리스트 가운데가 항상 root 노드이다.
중위 순회로 입력된 리스트를 왼쪽 부분 트리, 오른쪽 부분 트리로 쪼갠다.
'''