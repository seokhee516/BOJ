def swap(x,y, nx,ny):
    temp = board[x][y]
    board[x][y] = board[nx][ny]
    board[nx][ny] = temp

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 0: 행 확인 1: 열 확인
def check(x, y, board):
    result = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n: 
            if board[x][y] != board[nx][ny]: 
                swap(x,y, nx,ny)
                first_candy = board[x][0]
                temp = 1
                for j in range(1,n):
                    if first_candy != board[x][j]:
                        first_candy = board[x][j]
                        result = max(temp, result)
                        temp = 1
                    else:
                        temp += 1
                result = max(temp, result)
                first_candy = board[0][y]
                temp = 1
                for j in range(1,n):
                    if first_candy != board[j][y]:
                        first_candy = board[j][y]
                        result = max(temp, result)
                        temp = 1
                    else:
                        temp += 1
                result = max(temp, result)
                swap(x,y, nx,ny)
    return result

def run(n, board):
    result = 0
    # 행 확인
    for i in range(n):
        temp = 1
        for j in range(1,n):
            if board[i][j-1] != board[i][j]:
                result = max(result, check(i, j, board))
                temp = 1
            else:
                temp += 1
        result = max(result, temp)
    # 열 확인
    for i in range(n):
        temp = 1
        for j in range(1,n):
            if board[j-1][i] != board[j][i]:
                result = max(result, check(i, j, board))
                temp = 1
            else:
                temp += 1
        result = max(result, temp)
    return result
def n_same(board):
    for i in range(n):
        if board[i].count(board[i][0]) == n:
            return True
        for j in range(n-1):
            if board[j][i] != board[j+1][i]:
                return False
    return True

import sys
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    board.append(list(input().strip()))
if n_same(board):
    print(n)
else:
    print(run(n,board))
