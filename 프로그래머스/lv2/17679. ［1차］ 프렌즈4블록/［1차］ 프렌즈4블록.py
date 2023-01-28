def rm_check(m, n, b):
    rm = set()
    for i in range(m-1):
        for j in range(n-1):
            if b[i][j] == b[i+1][j] == b[i][j+1] == b[i+1][j+1] != '_':
                rm |= set([(i,j), (i+1,j), (i,j+1), (i+1,j+1)])
    for i, j in rm:
        b[i][j] = '_'
    while True:
        move = False
        for i in range(m-1):
            for j in range(n):
                if b[i][j] != '_' and b[i+1][j] == '_':
                    b[i+1][j] = b[i][j]
                    b[i][j] = '_'
                    move = True
        if not move:
            break
    return len(rm)
def solution(m, n, board):
    cnt = 0
    b = [list(board[i]) for i in range(m)]
    while True:
        cur = rm_check(m, n, b)
        if not cur:
            return cnt
        cnt += cur
    return cnt