import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def dfs(start=1, stack=[]):
    stack.append(start)
    for w in range(len(graph[start])):
        if graph[start][w] == 1 and (w not in stack):
            dfs(w, stack)
    return stack

print(len(dfs())-1)