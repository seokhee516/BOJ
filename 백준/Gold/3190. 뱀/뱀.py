import sys
input = sys.stdin.readline
from collections import deque

# 보드의 크기 입력
n = int(input())
# 사과의 개수 입력
k = int(input())

# n*n 보드 그래프 (0라인 있음)
graph = [[0] * (n+1) for _ in range(n+1)]

# 사과의 위치 입력
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

# 뱀의 방향 변환 횟수 입력
l = int(input())
# 뱀의 방향 변환 정보 입력
data = deque()
for _ in range(l):
    a, b = input().split()
    data.append((int(a), b))


# 이동할 네 방향 정의(상, 하, 좌, 우)
dxdy = {'up':(-1, 0), 'down':(1,0), 'left':(0, -1), 'right':(0, 1)}
# 방향 전환 함수
def direction(now, d_data):
    if now == 'right':
        if d_data =='D':
            now = 'down'
        else:
            now = 'up'
    elif now == 'left':
        if d_data =='D':
            now = 'up'
        else:
            now = 'down'
    elif now == 'up':
        if d_data =='D':
            now = 'right'
        else:
            now = 'left'
    elif now == 'down':
        if d_data =='D':
            now = 'left'
        else:
            now = 'right'
    dx, dy = dxdy[now]
    return dx, dy, now

# 뱀의 길이는 1, 맨위, 맨좌측에서 시작
snake = deque()
snake.append((1,1))

def dummy():
    # 처음에 오른쪽으로 이동
    snake.append((1,2))
    # 시간 1 시작
    time = 1
    # 현재 방향 오른쪽
    now = 'right'
    nx, ny = snake[-1]
    # 시간 정보, 방향 정보 확인
    t_data, d_data = data.popleft()
    while nx > 0 and ny > 0 and nx <= n and ny <= n:
        # 이동한 칸에 사과가 있다면
        if graph[nx][ny] == 1:
            # 사과가 없어지고 꼬리는 움직이지 않는다
            graph[nx][ny] = 0
        # 이동한 칸에 사과가 없다면
        else:
            # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다
            snake.popleft()
        # 현재시간과 시간 정보가 같다면
        if time == t_data:
            # 방향 전환 
            dx, dy , now = direction(now, d_data)
            # 새로운 시간 정보, 방향 정보 받기
            if data:
                t_data, d_data = data.popleft()
        else:
            dx, dy = dxdy[now]
        nx = dx + snake[-1][0]
        ny = dy + snake[-1][1]

        # 시간 추가
        time +=1
        # 자기자신의 몸과 부딪혔다면 종료
        if (nx,ny) in snake:
            return time
        # 다음칸으로 이동
        snake.append((nx,ny))

    return time

print(dummy())