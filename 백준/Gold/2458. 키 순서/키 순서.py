# 플로이드 와샬을 이용하여 갈 수 있는지 확인하기
# (특정 노드가 다른 노드를 가리키는 횟수 + 다른 노드가 특정 노드를 가리키는 횟수) == N-1이라면
# 특정 노드의 순서 알 수 있음
# if graph[a][k] == 1 and graph[k][b] == 1: graph[a][b] = 1
# 아이디어까지는 떠올랐는데 구현하는게 안떠오름!! 다시 생각해보니까 간단했넹

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 다른 노드를 거쳐 방문할 수 있는지 확인
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1
'''
graph 출력 예시 
- graph[a] a노드가 다른 노드 가르키는 횟수
- graph[i][a] 다른 노드가 a 노드 가르키는 횟수
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 1, 0, 1]
[0, 0, 1, 0, 0, 0, 1]
[0, 0, 1, 0, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 0]
'''
cnt = [0] * (n+1)
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == 1:
            cnt[a] += 1
            cnt[b] += 1
'''
cnt 출력 예시
[0, 4, 4, 3, 5, 4, 4]
'''
print(cnt.count(n-1)) # 키가 몇 번째인지 알 수 있는 학생 수