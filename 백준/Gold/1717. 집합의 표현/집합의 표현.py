import sys
sys.setrecursionlimit(100000) # 10만 회 재귀 제한
input = sys.stdin.readline
# 특정원소가 속한 집합 찾기
def find(x):
    # 루트 노드가 아니라면
    if parent[x] != x: # 루트 노드 찾을 때까지 재귀적 호출
        parent[x] = find(parent[x])
    return parent[x]
    
# 두 원소가 속한 집합 합치기
def union(a, b):
    a = find(a) # 루트 노드 찾기
    b = find(b)
    if a == b: # a, b의 루트노드가 같다면 동일한 집합
        return
    if a > b: # 다르다면 작은 루트 노드를 기준으로 합침
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a,b)
        # print(parent)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")