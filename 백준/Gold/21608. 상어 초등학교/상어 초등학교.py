n = int(input())
board = [[0]*n for _ in range(n)]
student = {}

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n**2):
    tmp = list(map(int, input().split()))
    k, v = tmp[0], tmp[1:]
    student[k] = v
    max = 0
    like = []
    for x in range(n):
        for y in range(n):
            if board[x][y] != 0:
                continue
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                elif board[nx][ny] in v:
                    cnt += 1
            if cnt > max:
                like = []
                like.append((x, y))
                max = cnt
            elif cnt == max:
                like.append((x, y))
    if len(like) == 1:
        a, b = like[0]
        board[a][b] = k
        continue
    else:
        max = 0
        empty = []
        for x, y in like:
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                elif board[nx][ny] == 0:
                    cnt += 1
            if cnt > max:
                empty = []
                empty.append((x, y))
                max = cnt
            elif cnt == max:
                empty.append((x, y))
    if len(empty) == 1:
        a, b = empty[0]
        board[a][b] = k
        continue
    else:
        empty.sort(key=lambda x:(x[0],x[1]))
        for a, b in empty:
            board[a][b] = k
            break
ans = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif board[nx][ny] in student[board[x][y]]:
                cnt += 1
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
print(ans)