import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
tetromino = [
    [(0,0),(1,0),(0,1),(1,1)], # ㅁ
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)], # ㅡ
    [(0,0),(1,0),(2,0),(2,1)],
    [(1,0),(1,1),(1,2),(0,2)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,1),(1,1),(2,1),(2,0)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(0,1),(1,0),(2,0)],
    [(0,0),(1,0),(1,1),(1,2)], # ㄴ
    [(0,0),(0,1),(1,1),(0,2)], # ㅜ
    [(0,0),(1,0),(1,1),(2,0)], # ㅏ
    [(1,0),(1,1),(0,1),(1,2)], # ㅗ
    [(0,1),(1,1),(1,0),(2,1)], # ㅓ
    [(0,0),(1,0),(1,1),(2,1)],
    [(1,0),(1,1),(0,1),(0,2)],
    [(2,0),(1,0),(1,1),(0,1)],
    [(0,0),(0,1),(1,1),(1,2)]]

answer = 0
def check(x,y):
    global answer
    for i in range(len(tetromino)):
        tmp = 0
        for j in range(4):
            nx = x + tetromino[i][j][0]
            ny = y + tetromino[i][j][1]
            if 0 <= nx < n and 0 <= ny < m:
                tmp += graph[nx][ny]
        answer = max(answer, tmp)

for i in range(n):
    for j in range(m):
        check(i, j)
print(answer)