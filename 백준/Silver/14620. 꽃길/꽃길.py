import sys
input = sys.stdin.readline

n= int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0,-1,1,0,0], [0,0,0,-1,1]

ans = 10000

def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // n
        y = flower % n
        if x == 0 or x == n-1 or y == 0 or y == n-1:
            return 10000
        for w in range(5):
            nx, ny = x+dx[w], y+dy[w]
            flow.append((nx, ny))
            ret += graph[nx][ny]
    if len(set(flow)) != 15:
        return 10000
    return ret

for i in range(n*n):
    for j in range(i+1,n*n):
        for k in range(j+1,n*n):
            ans = min(ans, ck([i,j,k]))
print(ans)