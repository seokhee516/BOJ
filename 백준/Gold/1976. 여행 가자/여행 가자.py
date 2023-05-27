import sys
sys.setrecursionlimit(100000) # 10만 회 재귀 제한
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

n = int(input())
m = int(input())
parent = [i for i in range(n)]
for i in range(n):
    link = list(map(int, input().split()))
    for j in range(n):
        if link[j] == 1:
            union(i,j)
parent = [-1] + parent
path = list(map(int, input().split()))
start = parent[path[0]]
for i in range(1, m):
    if parent[path[i]] != start:
        print("NO")
        break
else:
    print("YES")