# 알고리즘이 어렵다기보다는 수학적으로 아이디어를 생각해내는 것이 어려웠던 문제
import sys
import heapq
n = int(input())
town = []
people = 0
for _ in range(n):
    x, a = map(int, input().split())
    heapq.heappush(town, (x,a)) # x가 작은 순으로 넣기
    people += a # 인구 총합
cul = 0 # 인구 누적합
for i in range(n):
    tmp = heapq.heappop(town) # 위치가 작은 순서부터 뽑기
    cul += tmp[1] 
    if cul >= people / 2: # 인구의 누적 합이 전체 인구 절반 이상이면
        # //가 아니라 /로 나눠주어야 함 예를 들어 총합이 홀수인 경우 이를 절반으로 나눠준 값보다 큰 값이어야 누적합 절반 이상 원리가 적용되므로
        break
print(tmp[0])
'''
풀이 흔적
import sys
n = int(input())
town = [0] * (n+1)
for i in range(n):
    x, a = map(int, input().split())
    town[x] = a
# 모든 거리 계산해서 더해줌
dis = [0] * (n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        dis[i] += town[j] * abs(i-j)

print(dis.index(min(dis[1:])))

# -를 신경써주어야 하나?
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
town = []
for i in range(n):
    x, a = map(int, input().split())
    town.append((x,a))
print(town)
dis = defaultdict(int) # {지역위치 : 다른 지역과 인구 및거리 계산한 값}
for i in range(n):
    for j in range(n):
        dis[town[i][0]] += town[j][1] * abs(town[i][0]-town[j][0])
# print(dis)

dis = sorted(dis.items(), key=lambda x: (x[1], x[0]))
print(dis[0][0])
'''