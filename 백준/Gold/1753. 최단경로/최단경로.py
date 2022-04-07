'''
개선된 다익스트라 알고리즘
시간 복잡도 O(ElogV)
최단 거리가 가장 짧은 노드를 선택하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
# 방문 목록 체크 리스트 만들 필요 없음

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        '''이부분 이해 잘 안됨'''
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            # print("dist, now", dist, now, "distance[now] < dist", distance[now], dist)
            continue
        # 현재 노드와 인접한 다른 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    # 도달 할 수 없는 경우, INF 출력
    if distance[i] ==INF:
        print("INF")
    # 도달 할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

'''
입력 예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

노드 4에 대한 처리에서 4번 노드까지의 최단거리 (1) + 4번에서 3번 노드로 가는 거리 (3) 이라면 우선순위 큐에 (거리:4, 노드:3) 담김
그런데 노드 5에 대한 처리에서 5번 노드까지의 최단거리 (2) + 5번에서 3번 노드로 가는 거리 (2)인 3 이라면, 기존의 4보다 작다. 따라서 우선순위 큐에 (거리:3, 노드:3)이 담긴다.

if distance[now] < dist:
    continue
위 코드가 실행된다면
우선순위로 꺼낸 원소에는 3번(now)까지 최단 거리 4(dist)라는 정보가 들어있다. 하지만 현재 최단 거리 테이블에서 3번 노드까지 최단 거리(distance[now])는 3이다. 따라서 현재 노드인 3번(now)에 대해서는 무시(continue)하면 된다.
'''