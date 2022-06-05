import sys
input = sys.stdin.readline
# 집의 개수와 공유기의 개수 입력받기 
# 입력 범위가 10억이다 이분탐색으로 찾아야한다
n, c = map(int, input().split())

# 전체 집의 좌표 정보 입력 받기
array = [int(input()) for _ in range(n)]
array.sort()

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
    value = array[0]
    count = 1
    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1, n): # 앞에서부터 설치
        '''여기서부터 이해 잘 안됨..'''
        if array[i] >= value + mid:
            # print("array[i]", array[i],"value",value, "mid", mid)
            value = array[i]
            count += 1
            # print("count", count)
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        result = mid # 최적의 결과 저장
        start = mid + 1
        # print("start", start, "end", end)
    else: # C개 이상의 공유기를 설치할 수 있는 경우, 거리 감소
        end = mid -1

print(result)

'''
가장 인접한 두 공유기 사이의 거리가 4일때 
array[i] 8 value 1 mid 4 1집 위치) 4(거리)를 더한 5이상의 집이 없고 8이 최소 
count 2 공유기는 2개 설치

3(C)개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
end = 4-1 = 3
mid = (1+3) // 2 = 2 

가장 인접한 두 공유기 사이의 거리가 2일때
array[i] 4 value 1 mid 2 1(집 위치)+2(거리) 보다 큰 4 존재
count 2 공유기 설치
array[i] 8 value 4 mid 2 4 + 2(거리) 보다 큰 8 존재
count 3 공유기 설치

3(C)개 이상의 공유기를 설치할 수 있는 경우, 거리 증가
result = 2 일단 저장
start = 2+1 = 3
mid = (3+3) // 2 = 3
(여기서부터 start==end이기 때문에 더 이상 범위를 변경할 수 없다.)

array[i] 4 value 1 mid 3
count 2
array[i] 8 value 4 mid 3
count 3 

3(C)개 이상의 공유기를 설치할 수 있는 경우, 거리 증가
result = 3 일단 저장
start = 3+1 = 4

start(4) > end(3)
while 조건문 끝남

result = 3
'''