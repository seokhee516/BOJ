import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 플로이드 워셜 수행
for k in range(n):
    for a in range(n):
        for b in range(n):
            # a에서 b로 가는 간선 존재하거나 a에서 k를 거쳐 b로가는 간선 존재하면
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                # a에서 b로 가는 경로 존재
                graph[a][b] = 1
for i in graph:
    for j in i:
        print(j, end=' ')
    print()