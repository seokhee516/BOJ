from sys import stdin

input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] =  find(parent[x])
    return parent[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]
    print(number[x])

t = int(input())
for _ in range(t):
    k = int(input())
    parent, number = {}, {}
    for _ in range(k):
        a, b = input().strip().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)