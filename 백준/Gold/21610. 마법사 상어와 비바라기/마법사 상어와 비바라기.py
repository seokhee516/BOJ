n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split())) for _ in range(m)]

dx8 = ["empty", 0, -1, -1, -1, 0, 1, 1, 1]
dy8 = ["empty", -1, -1, 0, 1, 1, 1, 0, -1]

dx4 = [-1, -1, 1, 1]
dy4 = [-1, 1, -1, 1]

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for d, s in moves:
    moved_clouds = []
    for x, y in clouds:
        nx = (x + dx8[d] * s) % n
        ny = (y + dy8[d] * s) % n
        g[nx][ny] += 1
        moved_clouds.append((nx, ny))
    for x, y in moved_clouds:
        cnt = 0
        for d in range(4):
            nx = x + dx4[d]
            ny = y + dy4[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif g[nx][ny] > 0:
                cnt += 1
        g[x][y] += cnt
    new_clouds = []
    for x in range(n):
        for y in range(n):
            if (x, y) in moved_clouds or g[x][y] < 2:
                continue
            g[x][y] -= 2
            new_clouds.append((x, y))
    clouds = new_clouds

res = 0
for x in range(n):
    for y in range(n):
        res += g[x][y]
print(res)