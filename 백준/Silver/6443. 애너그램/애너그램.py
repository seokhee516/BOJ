import sys
input = sys.stdin.readline
def dfs():
    if len(tmp) == m:
        print("".join(tmp))
        return
    check = ""
    for i in range(m):
        if not visited[i] and check != s[i]: # check는 재귀 돌고 첫 방문일때는 ""
            visited[i] = True 
            tmp.append(s[i])
            check = s[i] # 중복된 수열 출력 방지 
            dfs()
            visited[i] = False
            tmp.pop()
n = int(input())
for _ in range(n):
    s = sorted(input().strip())
    m = len(s)
    visited = [False] * m # 방문해야 할 문자 구별
    tmp = []
    dfs()