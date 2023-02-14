import sys
sys.setrecursionlimit(10 ** 4) # 재귀 허용 깊이를 수동으로 늘려주는 코드
input = sys.stdin.readline

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break
    
# 후위 순회 (왼쪽-오른쪽-루트)
def postorder(start, end):
    if start > end:
        return
    root = tree[start]
    idx = start + 1
    
    while idx <= end:
        if root < tree[idx]: # 오른쪽 트리 index 찾기
            break
        idx += 1
    postorder(start+1, idx-1) # 왼쪽 트리 찾기
    postorder(idx, end) # 오른쪽 트리 찾기
    print(root) 
    
postorder(0, len(tree)-1) # start, end

'''
line 17-20
노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
line 21 idx-1이므로, 왼쪽 부터 찾음

line 22 왼쪽 트리
가장 왼쪽 트리는 start와 end가 같으므로, line 22, 23 return 끝나고
idx(start+1) > end 이므로 while 실행 안하고 root(tree[start]) 출력

line 23 오른쪽 트리
가장 왼쪽 노드 출력 후, 재귀적으로 실행됨 

line 24 root
재귀 다 끝나고 가장 마지막 root 노드 출력 
'''