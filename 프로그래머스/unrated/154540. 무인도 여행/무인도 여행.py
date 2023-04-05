from collections import deque

def solution(maps):
    answer = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    def bfs(x,y):
        res = int(maps[x][y])
        q = deque([(x,y)])
        visited[x][y] = True
        while q:
            x, y = q.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                    print(int(maps[nx][ny]))
                    res += int(maps[nx][ny])
                    visited[nx][ny] = True
                    q.append((nx, ny))
        return res
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                tmp = bfs(i,j)
                answer.append(tmp)

    return sorted(answer) if answer else [-1]