import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
combi = list(combinations(range(m),3))
for a, b, c in combi:
    sum = 0
    for i in range(n):
        sum += max(graph[i][a], graph[i][b], graph[i][c])
    ans = max(ans, sum)
print(ans)