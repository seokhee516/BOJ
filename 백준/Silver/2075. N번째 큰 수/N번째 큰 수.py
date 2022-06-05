import heapq
import sys
input = sys.stdin.readline
# 입력할때 처리해보기
n = int(input())
# 숫자 정보 입력
heap = []
for _ in range(n):
    line = list(map(int, input().split()))
    for l in line:
        # 일단 큐에 넣기
        heapq.heappush(heap, l)
        # 큐의 크기가 n 보다 크면
        if len(heap) > n:
            # 큐에서 가장 작은 값 빼기
            heapq.heappop(heap)
# N번째 큰 수이므로 가장 큰 N개중 가장 작은 값 출력
print(heap[0])

'''
# 큰순으로 넣고 마지막에 비교하기 - 요것도 메모리 초과
n = int(input())
# 숫자 정보 입력
data = []
for _ in range(n):
    line = list(map(int, input().split()))
    # 오름차순으로 정렬
    line.sort()
    data.append(line)

def num_check(n,data):
    # 가장 마지막줄 큰수들이므로 마지막에서 시작
    heap = data[n-1]
    heapq.heapify(heap)
    for i in range(n-2,-1,-1):
        for j in range(n-1,-1,-1):
            # 힙의 가장 작은 값이 데이터의 가장 큰 수보다 작다면
            if heap[0] < data[i][j]:
                # 힙의 가장 작은 수 빼주고
                heapq.heappop(heap)
                # 데이터의 가장 큰 수 넣어줌
                heapq.heappush(heap, data[i][j])
            else:
                return heap
# N번째 큰 수이므로 가장 큰 N개중 가장 작은 값 출력
print(num_check(n,data)[0])
'''
'''
# 냅다 넣기 -> 메모리 초과 ㅎㅎ
n = int(input())
heap = []
for i in range(n):
    line = map(int, input().split())
    for l in line:
        heapq.heappush(heap, -l)

num = -heapq.nsmallest(n, heap)[n-1]
print(num)
'''