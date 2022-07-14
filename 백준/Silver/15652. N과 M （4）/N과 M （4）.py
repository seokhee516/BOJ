import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tmp = []
def dfs():
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(1, n+1):
        # if i not in tmp:
        if not tmp:
            tmp.append(i)
            dfs()
            tmp.pop()
        else:
            if max(tmp) <= i:
                tmp.append(i)
                dfs()
                tmp.pop()
dfs()