import sys
from collections import deque
N = int(sys.stdin.readline().strip())
lst=[]
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().strip())))
#bfs
queue = deque()
cnt = 0
house = []

for i in range(N):
    for j in range(N):
        if lst[j][i] == 1:
            cnt += 1
            queue.append([i,j])
            h = 0 # 단지 수 초기화
            while queue:
                v = queue.popleft()
                a = v[0]
                b = v[1]
                lst[b][a] = 0
                h += 1 # 단지 수 더하기
                # 네 방향 확인, 범위 제한
                if a+1<N and lst[b][a+1] == 1: # 우
                    queue.append([a+1, b])
                    lst[b][a+1] = 0
                if a-1>=0 and lst[b][a-1] == 1: # 좌
                    queue.append([a-1, b])
                    lst[b][a-1] = 0
                if b-1>=0 and lst[b-1][a] == 1: #상
                    queue.append([a, b-1])
                    lst[b-1][a] = 0
                if b+1<N and lst[b+1][a] == 1: # 하
                    queue.append([a, b+1])
                    lst[b+1][a] = 0
            house.append(h) # 출력하기 위해 리스트에 담기
print(cnt)
for x in sorted(house):
    print(x)