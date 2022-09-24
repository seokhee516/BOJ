import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []
def back():
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(n):
        tmp.append(nums[i])
        back()
        tmp.pop()
                
back()