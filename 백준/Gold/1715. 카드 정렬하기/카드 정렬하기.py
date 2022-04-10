import sys
import heapq
input = sys.stdin.readline


n = int(input())
array = []
# 가장 작은 순으로 array에 담기 
# deque는 sort가 안되고, list는 가장 작은 카드 묶음을 뽑기 위한 popleft가 안됨
for i in range(n):
    heapq.heappush(array, int(input()))

# result : 최소 비교 횟수, temp : 가장 작은 두 카드 묶음 합
result = 0
temp = 0

# array의 길이가 1이 될때까지(원소가 하나 들어오거나, 카드 묶음 합과 남은 원소 더한 값일때)
while(len(array)) != 1:
    # 첫번째 카드
    one = heapq.heappop(array)
    # 두번째 카드
    two = heapq.heappop(array)
    temp = one + two
    result += temp
    # 카드 묶음 합을 다시 array에 넣어줌
    heapq.heappush(array, temp)

# 결과 출력
print(result)