import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []
def dfs():
    if len(tmp) == m:
        print(*tmp)
        return
    check = 0 
    for i in range(n):
        if check != nums[i]:
            tmp.append(nums[i])
            check = nums[i] # 중복된 수열 출력 방지 
            dfs()
            tmp.pop()
dfs()