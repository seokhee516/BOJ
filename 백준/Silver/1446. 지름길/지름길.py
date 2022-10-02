import sys
import heapq
input = sys.stdin.readline
INF = 1e9
N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)
# 현재에서 다음 칸으로 가는 거리 입력
for i in range(D):
    graph[i].append((i+1, 1))
# 지름길 거리 입력
for _ in range(N):
    start, end, length = map(int, input().split())
    if end > D: continue
    graph[start].append((end,length))
# print(graph)
# 다익스트라 알고리즘 
def dijkstra(start):
    q = []
    heapq.heappush(q, (start,0))
    distance[start]=0
    while q:
        # 가장 최단 거리가 짧은 거리 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드라면 무시
        if distance[now] < dist: continue
        # cost: 현재 노드까지 최단 비용 + 현재 노드를 거쳐 인접 노드로 가는 비용
        for next in graph[now]:
            cost = dist + next[1]
            # distance[next[0]] : 현재 노드를 거치기 전까지 최단 비용
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                # q에 인접노드로 이동한 최단비용 적은 순으로 기록 (최소 힙)
                heapq.heappush(q, (cost, next[0]))
dijkstra(0)
print(distance[D])