def solution(n, roads, k):
    ans = 0
    INF = int(1e9)
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for road in roads:
        a, b = road[0], road[1]
        # 도로 여러개일 수 있으므로 최소화
        graph[a][b] = min(graph[a][b], road[2])
        graph[b][a] = graph[a][b]
    # 플로이드 와샬
    for f in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                # 자기 자신 가는 시간 0
                if a == b:
                    graph[a][b] = 0
                # 다른 노드를 거쳐 방문할 수 있는지 확인
                else:
                    graph[a][b] = min(graph[a][b], graph[a][f] + graph[f][b])
    # k 이하 시간에 배달 가능 한 마을 개수
    ans = len([i for i in range(1, n+1) if graph[1][i] <= k])

    return ans