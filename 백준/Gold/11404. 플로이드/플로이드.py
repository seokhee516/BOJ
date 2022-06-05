import sys
input = sys.stdin.readline
INF = int(1e9) # 비용은 100,000 보다 작거나 같은 자연수
# 도시의 개수 n 버스의 개수 m 입력
n = int(input())
m = int(input())

# 2차원 리스트를 만들고, 모든 값을 최대로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 시작 도시와 도착 도시가 같은 비용 0인 경우 제외
    if graph[a][b] > c:
        graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
            if a == b:
                graph[a][b] = 0
            # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다. -> k를 거쳐갈 수 있음
            else:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        # 갈 수 없는 경우 0 출력
        if graph[a][b] == INF:
            print(0, end=" ")
        # 갈 수 있는 경우 거리 출력
        else:
            print(graph[a][b], end=" ")
    print()