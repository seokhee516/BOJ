import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * n]
for _ in range(n):
    lst = list(map(int, input().split()))
    lst.insert(0,0)
    for i in range(1, n+1):
        lst[i] = lst[i] + lst[i-1] # 누적합 구하기
    graph.append(lst)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for i in range(x1,x2+1):
        ans += (graph[i][y2]-graph[i][y1-1]) # 구간합 구하기
    print(ans)