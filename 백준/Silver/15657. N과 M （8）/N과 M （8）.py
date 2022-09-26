import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []
def back(start):
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(start, n):
        tmp.append(nums[i])
        back(i)
        tmp.pop()
            
back(0)