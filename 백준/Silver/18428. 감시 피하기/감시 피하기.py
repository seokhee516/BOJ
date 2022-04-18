'''
'연구소' 문제랑 비슷하게 풀어볼려했는데, 선생님이 이동하는 위치가 상하좌우를 다 가는 방식이 아니라 상하좌우 쭉 확인하는 방식이라 구현을 못했다... 
'''
'''
# 내풀이^^....
from collections import deque
# N 입력
n = int(input())

# 복도 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(input().strip().split()))
# print(graph)
# 장애물을 설치한 뒤 맵 리스트
temp = [['X'] * n for _ in range(n)]

# 감시 피할 수 있는지 여부
result = ''

# BFS를 이용해 선생님의 감시 범위 확인하기
# 4가지 이동 방향에 대한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def teacher(x, y):
    global result
    queue = deque()
    queue.append((x,y))
    
    # 상하좌우 감시
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        while queue:
            x, y = queue.popleft()
            # 맵 안에 있는 경우
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if temp[nx][ny] == 'O':
                    break
                if temp[nx][ny] == 'S':
                    result = 'NO'
                    return
                if temp[nx][ny] == 'X':
                    temp[nx][ny] = 'T'
                    queue.append((nx,ny))

# DFS를 이용해 장애물 설치하면서, 감시할 수 있는지 확인
def dfs(cnt):
    global result
    # 장애물이 3개 설치된 경우
    if cnt == 3:
        result = 'YES'
        for i in range(n):
            for j in range(n):
                temp[i][j] = graph[i][j]
        # 감시하기
        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'T':
                    teacher(i,j)
        return
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                cnt += 1
                dfs(cnt)
                graph[i][j] = 'X'
                cnt -= 1
dfs(0)
print(result)

'''

'''
답안 예시
장애물을 3개 설치하는 경우의 수는 N x N 이며, N은 최대 6이다. 따라서 최악의 경우는 36C3 으로 10,000 이하의 수이므로 따라서 모든 조합을 찾기 위해 DFS 혹은 BFS를 이용하거나 파이썬 조합 라이브러리를 이용할 수 있다.
또한 선생님의 위치에서 상하좌우의 위치를 확인하며 학생이 있는지 확인한다.
답안 예시에서는 꼭 DFS/BFS가 아니라 조합을 이용해서 풀었는데, 
생각해보니 경로를 탐색하는 알고리즘이니까 모든 경우를 따지는 조합을 사용해서 풀 수도 있겠다. 
기억해두자!
'''
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도의 정보 (N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 경우 위치 저장
        if board[i][j] == 'T':
            teachers.append((i,j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i,j))

# 특정한 방향으로 감시를 진행 (학생 발견 : True, 학생 미발견 : False)
def watch(x,y, direction):
    '''상하좌우 쭉 확인하는 방식 구현 방법'''
    # 왼족 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y += 1
    # 위족 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에 한명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            '''오... direction 을 숫자로 지정해서 방향을 이렇게 표시할 수도 있구나'''
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부

# 빈 공간 3개 뽑는 모든 조합 확인
for data in combinations(spaces,3):
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발션한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')