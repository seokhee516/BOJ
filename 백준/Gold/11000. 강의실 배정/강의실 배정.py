import heapq
import sys
input = sys.stdin.readline

# N의 개수 입력
N = int(input())
# 강의실 정보 입력
data = []
for _ in range(N):
    S, T = map(int, input().split())
    data.append((S,T))
# 시작시간 가장 빠른 순으로 정렬
data.sort()
# 비교를 위해 첫번째 강의시간 넣기
# 끝나는 시간 빠른 순으로 정렬할것이기 때문에 끝나는 시간만 넣기
heap = [data[0][1]]

# 강의실 시간 비교
for i in range(1, N):
    # 현재 회의 끝나는 시간이 다른 회의 시작 시간 보다 작거나 같을 때
    if heap[0] <= data[i][0]:
        # 한 강의실에서 진행
        heapq.heappop(heap) # 현재 강의실 빼주기
        heapq.heappush(heap, data[i][1]) # 다른 회의 넣기
    # 회의 끝나는 시간이 다음 회의 시작보다 클때 
    else:
        # 강의실 새로 추가
        heapq.heappush(heap, data[i][1])
# 강의실의 개수 출력
print(len(heap))

'''
자꾸 틀렸던 이유...
처음 강의실에 배정할때는 시작시간이 가장 빠른 것부터 넣어야함. 강의실을 적게 사용할려면 시작시간과 종료시간 간격이 짧아야 하므로, 시작시간이 빠른 것들로 먼저 정렬해놓고! 이것을 끝나는 시간이 빠른 것들과 비교해주어야 한다~ 
주의할 점은!!! 
1. heapq.heappush로 넣으면 트리형식으로 넣기 때문에 for 문을 돌면 시작 시간 빠른 순으로 나오지 않는다! 따라서 sort로 리스트를 정렬 해주어야 한다.
2. data와 heap의 정렬 순서가 다른데 for 문을 돌때 data를 heap에 넣으면 비교가 어려워지므로 heap에는 끝나는 시간만 넣어준다!
큐에 꼭 두가지 모두 넣어야 된다는 생각을 버렷!!!!

'이중 우선순위 큐'문제에서는 두가지 기준을 쓸려면 힙을 두개를 만들어줬는데 그건 각각의 값을 따로 저장해야해서 그랬던거구.. 시간초과 제한도 좀 많았던것 같당... 어떨때 쓰는지는 잘 구분이 안가넹ㅎㅎ
'''