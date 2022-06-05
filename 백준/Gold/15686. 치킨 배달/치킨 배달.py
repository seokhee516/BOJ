import sys
input = sys.stdin.readline
# n 도시의 크기, m 폐업시키지 않을 치킨집
n, m = map(int, input().split())
# 도시의 정보 입력
home = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 집의 정보 저장
            home.append((i,j))
        if data[j] == 2: # 치킨집의 정보 저장
            chicken.append((i,j))

'''
# 치킨 집을 기준으로 집과의 모든 거리를 담을 리스트
distance_list = []
for i in range(len(chicken)):
    # 한 줄당 하나의 치킨집에서 집까지의 거리
    distance = [0] * len(home)
    for j in range(len(home)):
        distance[j] = abs(home[j][0]-chicken[i][0]) + abs(home[j][1]-chicken[i][1])
    distance_list.append(distance)
# 거리합이 작은 순으로 정렬
distance_list = sorted(distance_list, key=lambda x:sum(x))

# 폐업시키지 않을 M개의 치킨집 고르기
distance_list = distance_list[:m]
# print(distance_list[:m])
# 첫번째 줄 저장
result = distance_list[0]
# 다음 줄 돌면서 첫번째 값보다 작으면 저장
for i in range(1,m):
    for j in range(len(home)):
        result[j] = min(result[j], distance_list[i][j])
# 도시의 치킨 거리 출력
print(sum(result))

처음에는 이렇게 풀었는데 틀렸다...
폐업시킬 치킨집은 딱 M개가 아니라 최대 M개라서 M개를 고르는게 아니었고, 도시의 치킨 거리 합이 작은 순으로 M개가 아니라 합이 더 크더라도 선택한 치킨 집이 각각의 집들이랑 가까우면 최소가 된다... 
결국 답 찾아봤다..ㅠㅠ
'''

from itertools import combinations
# 치킨집 후보를 조합으로 모두 찾음
candidates = list(combinations(chicken, m))
INF = int(1e9) # 무한의 값

# 거리를 저장할 리스트
distance_list = []
# 후보들 모두 확인
for candidate in candidates:
    # result 도시의 치킨 거리 저장
    result = 0
    # 모든 집에 대하여
    for hx,hy in home: 
        temp = INF
        # 후보 치킨 집들 중에서 집과 가까운 거리 저장
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        # 최소 치킨 거리를 도시의 치킨 거리에 저장
        result += temp
    # 집에 대한 for 문 끝나면 도시의 치킨 거리를 리스트에 저장
    distance_list.append(result)

# 도시의 치킨 거리 최솟값 출력
print(min(distance_list))

'''
나는 거리를 먼저 구하고 후보를 뽑을려했는데, 
'합이 더 크더라도 선택한 치킨 집이 각각의 집들이랑 가까우면 최소'이므로, 후보를 먼저 뽑고 거리 구하는게 모든 경우를 확인할 수 있다.
그리고 거리 for 문 돌때 for hx,hy in home: 이런식으로 쓰니까 거리 정보를 더 잘 알아볼 수 있다.
'''