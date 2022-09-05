def solution(grid):
    ans = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    lx, ly = len(grid), len(grid[0])
    # 방문 표시
    visited = [[[False]*4 for _ in range(ly)] for _ in range(lx)]
    for x in range(lx):
        for y in range(ly):
            # 네 방향 모두 확인
            for d in range(4):
                # 방문 했다면 넘어가기
                if visited[x][y][d]:
                    continue
                else:
                    light = 0
                    # 방문하지 않았다면
                    while not visited[x][y][d]:
                        visited[x][y][d] = True # 방문 표시
                        light += 1 # 빛의 경로 추가
                        if grid[x][y] == "L": # 좌회전
                            d = (d-1) % 4 # 방향 범위 지키기
                        if grid[x][y] == "R": # 우회전
                            d = (d+1) % 4
                        x = (x+dx[d]) % lx # 넘어갈 경우 반대쪽으로
                        y = (y+dy[d]) % ly
                    ans.append(light)
    # 오름차순 정리
    ans.sort()
    return ans