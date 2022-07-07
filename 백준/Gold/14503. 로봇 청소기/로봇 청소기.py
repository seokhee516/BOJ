import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,0,1,0] # 북, 동, 남, 서
dy = [0,1,0,-1]

def cleaning(x, y, d):
    answer = 0
    cnt = 0
    while True:
        # 현재 위치 청소
        if graph[x][y] == 0:
            answer += 1
            graph[x][y] = -1 # 청소 위치 표시
        while cnt != 4:
            # 왼쪽 방향으로 회전
            d -= 1
            if d == -1:
                d = 3
            # 2a 실행 횟수 세기
            cnt += 1
            # 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면 한칸 전진
            nx = x + dx[d]
            ny = y + dy[d]
            if graph[nx][ny] == 0:
                # 1번으로 돌아감
                x = nx
                y = ny
                cnt = 0
                break
        if cnt == 4: # 연속 네번 실행
            bx = x - dx[d]
            by = y - dy[d]
            if graph[bx][by] == 1:
                # 작동 멈춤
                break
            else:
                cnt = 0
                x = bx
                y = by
    return answer

print(cleaning(r, c, d))
