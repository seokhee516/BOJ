'''
최소 힙과 최대힙을 구현했으나, 따로 동작하면 값이 달라진다. 따라서 구현한 최소힙과 최대힙을 동기화 시켜주어야 한다. 이를 위해 힙에 푸쉬할때 각 노드를 유일하게 구분할 식별자 id 값을 넣어준다. 반복문이 몇 번 수행되었는지를 가리키는 변수 i를 유일성을 만족시키는 id로 사용할 수 있다. 

id 값은 튜플의 형태로 넣어준다. 우선순위 큐는 첫 번째 원소를 기준으로 판단하기 때문에 id를 튜플의 두 번째 원소로 넣어주면 힙의 구동에도 아무런 문제가 없다.

식별자는 동기화 작업에 활용된다. 먼저 삽입 시에는 따로 동기화할 필요가 없다. 하지만 삭제 시에는 최소힙은 최소값만 pop할 수 있을 뿐 최대값을 삭제하는 방법이 없다. 
따라서 삭제 시 id를 기준으로 해당 노드가 다른 힙에서 삭제된 노드인지 아닌지를 판단한다. 이미 삭제된 노드일 경우 삭제되지 않은 노드가 나올때까지 모두 버린다. 이후 삭제 대상 노드가 등장하면 삭제한다. id별 상태를 기록하기 위해 visited 플래그 리스트를 사용한다.

'''

import heapq
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    # 최소힙과 최대힙 두개 만들기
    min_heap = []
    max_heap = []
    # id 값을 넣어줄 플래그 리스트
    visited = [False] * 1000001

    for i in range(k):
        x, y = map(str, input().split())
        if x =='I':
            heapq.heappush(min_heap, (int(y),i)) # 튜플의 형태로 값과 id값을 넣어줌
            heapq.heappush(max_heap, (-int(y),i))
            visited[i] = True # id 상태 기록 True이면 삭제되지 않은 상태
        else: # 최소값
            if y == '-1':
                # 최소힙이므로 가장 작은 요소는 루트인 min_heap[0]이다
                # min_heap[0][1]은 id
                while min_heap and not visited[min_heap[0][1]]: # 이미 삭제된 노드인 경우 (visited가 False)
                    heapq.heappop(min_heap) # 삭제되지 않은 노드가 나올때까지 버리기
                if min_heap: # 존재하는 경우
                    visited[min_heap[0][1]] = False # 삭제 표시 후 최소값 뽑기
                    heapq.heappop(min_heap)
            else: # 최대값 
                # 최대힙 역시 -로 들어갔으므로 가장 큰 요소는 max_heap[0]이다
                while max_heap and not visited[max_heap[0][1]]: # 이미 삭제된 노드인 경우 (visited가 False)
                    heapq.heappop(max_heap) # 삭제되지 않은 노드가 나올때까지 버리기
                if max_heap: # 존재하는 경우
                    visited[max_heap[0][1]] = False # 삭제 표시 후 최대값 뽑기
                    heapq.heappop(max_heap)
    
    # 최대값,최소값을 뽑고 삭제 처리를 해주었으므로,삭제된 노드가 visited에 들어가 있을 수 있다.
    # 따라서 한번 더 처리 (삭제 표시는 visited에 따로 하므로 값 뽑기 전과 후 상관 없다)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
'''
최소힙과 최대힙 두개 만들기 - 시간 초과
for _ in range(t):
    k = int(input())
    # 최소힙과 최대힙 두개 만들기
    min_heap = []
    max_heap = []

    for i in range(k):
        x, y = map(str, input().split())
        if x =='I':
            heapq.heappush(min_heap, int(y))
            heapq.heappush(max_heap, -int(y))
        else:
            if min_heap:
                if y == '-1':
                    min_value = heapq.heappop(min_heap)
                    max_heap.remove(-min_value)
                else:
                    max_value = -heapq.heappop(max_heap)
                    min_heap.remove(max_value)
            else: # 비었는데 적용하면 무시
                pass
    if min_heap and max_heap:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))
    else:
        print("EMPTY")
'''
'''
nlargest 사용 - 시간 초과
for _ in range(t):
    k = int(input())
    heap = []
    for i in range(k):
        x, y = input().split()
        if x =='I':
            heapq.heappush(heap, int(y))
        else:
            if heap:
                if y == '-1':
                    heapq.heappop(heap)
                else:
                    # 최소 힙에서 최대값 뽑기 
                    # nlargest(n,리스트) 리스트에서 가장 큰 n개의 수 뽑음
                    heap = heapq.nlargest(len(heap), heap)[1:] # 1 부터 슬라이싱 최대값 제외
                    # 다시 최소힙으로 만들어줌
                    heapq.heapify(heap)
            else: # 비었는데 적용하면 무시
                pass
    if heap:
        print(heapq.nlargest(1, heap)[0], heapq.heappop(heap))
    else:
        print("EMPTY")

'''