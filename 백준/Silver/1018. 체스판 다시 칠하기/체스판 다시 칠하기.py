import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
# print(graph)
res = []
for x in range(n-7):
    for y in range(m-7):
        first_w = 0
        first_b = 0
        for i in range(x,x+8):
            for j in range(y,y+8):
                if (i + j) % 2 == 0:
                    if graph[i][j] != 'W':
                        first_w += 1
                    else:
                        first_b += 1
                else:
                    if graph[i][j] != 'B':
                        first_w += 1
                    else:
                        first_b += 1
        res.append(first_w)
        res.append(first_b)
print(min(res))