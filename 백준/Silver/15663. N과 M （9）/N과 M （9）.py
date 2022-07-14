import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n # 방문해야 할 숫자 구별
tmp = []
def dfs():
    if len(tmp) == m:
        print(*tmp)
        return
    check = 0 
    for i in range(n):
        if not visited[i] and check != nums[i]: # 첫 방문일때
            visited[i] = True 
            tmp.append(nums[i])
            check = nums[i] # 중복된 수열 출력 방지 
            dfs()
            visited[i] = False
            tmp.pop()
dfs()

'''
check = nums[i] 없을 때
4 2
9 7 9 1
----------------------
1 7
1 9
1 9 # 중복
7 1
7 9 
7 9 # 중복
9 1
9 7
9 9 
9 1 # 중복
9 7
9 9

check = nums[i] 있을 때
4 2
9 7 9 1
----------------------
1 7
1 9
7 1
7 9
9 1
9 7
9 9
'''