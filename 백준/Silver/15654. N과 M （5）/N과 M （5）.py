import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n # 방문해야 할 숫자 구별
tmp = []
def dfs():
    if len(tmp) == m: # 길이가 M 일때 출력
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