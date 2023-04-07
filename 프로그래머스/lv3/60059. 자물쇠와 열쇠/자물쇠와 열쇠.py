def rotate(array, d):
    N = len(array)
    ret = [[0]*N for _ in range(N)]
    if d == 0:
        for r in range(N):
            for c in range(N):
                ret[c][N-r-1] = array[r][c]
    elif d == 1:
        for r in range(N):
            for c in range(N):
                ret[N-r-1][N-c-1] = array[r][c]
    elif d == 2:
        for r in range(N):
            for c in range(N):
                ret[N-c-1][r] = array[r][c]
    else:
        return array
    return ret

def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
    for i in range(1,n*2):
        for j in range(1, n*2):
            for d in range(4):
                r_key = rotate(key, d)
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += r_key[x][y]
                if check(new_lock):
                    return True
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= r_key[x][y]

    return False