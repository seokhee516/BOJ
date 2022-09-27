import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
tmp = []
def back():
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(len(nums)):
        if len(tmp) == 0 or tmp[-1] <= nums[i]:
            tmp.append(nums[i])
            back()
            tmp.pop()
                
back()