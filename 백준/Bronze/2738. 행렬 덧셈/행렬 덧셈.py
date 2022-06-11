n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    lst2 = list(map(int, input().split()))
    for j in range(m):
        lst[i][j] += lst2[j]
        
for i in range(n):
    for j in range(m):
        print(lst[i][j], end=' ')
    print()