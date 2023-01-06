import sys
input = sys.stdin.readline
n = int(input())
sign = input().split()
ans = []
visited = [False] * 10

def check(x, y, op):
    if op == '<':
        return x<y
    if op == '>':
        return x>y
    return False

def solve(idx, s):
    if idx == n+1:
        ans.append(s)
        return

    for i in range(10):
        if visited[i]:
            continue
        if idx == 0 or check(s[idx-1], str(i), sign[idx-1]):
            visited[i] = True
            solve(idx+1, s+str(i))
            visited[i] = False
solve(0, '')

ans.sort()
print(ans[-1])
print(ans[0])