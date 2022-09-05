import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())
for _ in range(t):
    control = input().strip()
    move = [0,0]
    dir = 0
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for c in control:
        if c == 'F':
            move[0] += dx[dir]
            move[1] += dy[dir]
        if c == 'B':
            move[0] -= dx[dir]
            move[1] -= dy[dir]
        if c == 'L':
            dir = (dir-1) % 4
        if c == 'R':
            dir = (dir+1) % 4
        max_x = max(max_x, move[0])
        max_y = max(max_y, move[1])
        min_x = min(min_x, move[0])
        min_y = min(min_y, move[1])
    print((max_x-min_x)*(max_y-min_y))