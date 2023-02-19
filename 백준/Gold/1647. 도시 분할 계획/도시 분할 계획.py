def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a == b: 
        return
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
        
v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
# print(edges)
res = 0
last = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a,b)
        res += cost
        last = cost
print(res-last)