import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())

# 인구수 그래프 저장
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 네 방향 확인
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인구 처리 함수
def process(x, y, index):
    # (x,y)와 연결된 연합 정보 담는 리스트
    united = []
    united.append((x,y))
    # BFS를 위한 큐
    queue = deque()
    queue.append((x,y))
    '''
    연합이 여러개 생기는 경우를 위해 연합 번호 할당하는 방식
    이렇게 하면 국경이 열리지 않는 경우에도 다른 번호가 할당되고 각각을 처리할 수 있겠구나!
    나는 True False로 할려했더니 연합이 여러개 생기는 경우를 처리하지 못했다..ㅠㅠ
    '''
    union[x][y] = index # 현재 연합의 변호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    cnt = 1 # 현재 연합의 국가 수

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            '''
            and not union[nx][ny]==-1 요걸로 방문 여부 확인
            if로 사잇값 비교할때 바로써줘도 됨
            '''
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆 나라 인구 차이가 L명 이상 R명 이하라면
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    queue.append((nx,ny))
                    # 연합에 추가
                    union[nx][ny] = index # 연합 번호 할당
                    summary += graph[nx][ny]
                    cnt += 1
                    united.append((nx,ny)) # 연합 위치 추가
    # 연합국가 인구분배
    for i, j in united:
        graph[i][j] = summary // cnt   
    return cnt

# 인구이동 횟수 
result = 0

# 더 이상 인구 이동 없을 때까지 반복
while True:
    union = [[-1]* n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 국가가 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    '''
    index 와 n*n이 같다는 건 union이 모두 -1이어서 처리해줄 국가가 없다는 의미
    '''
    if index == (n*n): 
        break
    result += 1

print(result)

'''
내 풀이.. 
True False로 다 풀려하니까 연합이 여러개 있을때 처리가 안됨
거기에 연합 존재 유무도 따로 변수를 만들어줘야 해서 복잡함
답안 예시에서는...
union : 연합 국가 번호 매겨서 여러 연합일때 처리, 연합 존재 여부 처리, 방문여부 확인
united : 연합 위치 정보 넣어서 인구분배할때 활용
나머지 버릴때는 math.trunc 말고 그냥 // 쓰자

import sys
input = sys.stdin.readline
import math
from collections import deque

n, l, r = map(int, input().split())

# 인구수 그래프 저장
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 국경선 정보 저장 그래프 False 국경선 닫힘
border = [[False] * n for i in range(n)]

# 연합 존재 유무 
union = False
# 인구이동 횟수 
result = 0

# 국경선 열기 BFS
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def check(x, y):
    global union
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                dif = abs(graph[nx][ny]-graph[x][y])
                if l <= dif and dif <= r and not border[nx][ny]:
                    border[nx][ny] = True
                    border[x][y] = True
                    union = True # 연합 존재 표시
                    queue.append((nx,ny))
    if union:
        sum = 0
        cnt = 0
        for i in range(n):
            for j in range(n):
                if border[i][j]:
                    sum += graph[i][j]
                    cnt += 1


# 연합 존재하는지 확인
for i in range(n):
    for j in range(n):
        check(i, j)
while union: # 연합이 존재한다면
    # 인구이동 시작
    result += 1
    sum = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if border[i][j]:
                sum += graph[i][j]
                cnt += 1
    for i in range(n):
        for j in range(n):
            if border[i][j]:
                graph[i][j] = math.trunc(sum / cnt)
                border[i][j] = False # 국경선 닫기
    union = False # 연합 해체
    print(graph)
    # 연합 있는지 다시 확인
    for i in range(n):
        for j in range(n):
            check(i, j)


print(result)
'''