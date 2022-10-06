import sys
input = sys.stdin.readline
n, m = map(int, input().split())
password = sorted(list(input().split()))
res = []
def dfs(start):
    if len(res) == n:
        c, v = 0, 0 # 자음, 모음
        for x in res:
            if x in 'aeiou':
                v+=1
            else:
                c+=1
        if v >= 1 and c >=2: # 최소 한 개의 모음과 최소 두 개의 자음
            print("".join(res))
        return
    for i in range(start, m):
        res.append(password[i])
        dfs(i+1)
        res.pop()
                
dfs(0)