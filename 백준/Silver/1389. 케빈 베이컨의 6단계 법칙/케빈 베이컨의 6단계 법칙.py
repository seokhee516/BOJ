import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # a에서 b, b에서 a로 가는 비용 1
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드 워셜 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a==b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
for a in range(0, n+1):
    for b in range(0, n+1):
        if graph[a][b] == INF:
            graph[a][b] = 0

res = INF
res_idx = 0
for i in range(n, 0, -1):
    if res >= sum(graph[i]):
        res = sum(graph[i])
        res_idx = i
print(res_idx)
