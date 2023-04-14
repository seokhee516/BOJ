def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]
    for a, b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1, -1]:
                    continue
                if board[i][k] == board[k][j] == 1: # i가 k를 이기고, k가 j를 이기면
                    board[i][j] = 1 # i는 j를 이긴다
                    board[k][i] = board[j][k] = board[j][i] = -1 # k가 i에게 지고, j가 k에게 지면, j는 i에게 진다
    for row in board:
        if row.count(0) == 1:
            answer += 1
    return answer