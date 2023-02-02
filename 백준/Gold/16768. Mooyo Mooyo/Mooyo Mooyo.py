import sys
from collections import deque

def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]

input = sys.stdin.readline
N, K = map(int, input().split())
M = [list(input().strip()) for _ in range(N)]
ck = new_array(N) # 그룹에 있는가
ck2 = new_array(N) # 지워도 되는가

dx, dy = [-1,1,0,0], [0,0,-1,1]

def dfs(x, y):
    ck[x][y] =True
    ret = 1
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret
        

def dfs2(x, y, val):
    ck2[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck2[xx][yy] or M[xx][yy] != val:
            continue
        dfs2(xx, yy, val)


def down():
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] != '0':
                tmp.append(M[j][i])
        for j in range(N-len(tmp)):
            M[j][i] = '0'
        for j in range(N-len(tmp), N):
            M[j][i] = tmp[j - (N-len(tmp))]
            
while True:
    exit = False
    ck = new_array(N)
    ck2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i,j) # 개수 세기
            if res >= K:
                dfs2(i, j, M[i][j]) # 지우기
                exit = True
    if not exit:
        break
    down() # 내리기

for i in M:
    print(''.join(i))
