import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []
def back(start):
    if len(tmp) == m:
        print(*tmp) # 예쁘게 출력
        return
    for i in range(start, n):
        if nums[i] not in tmp:
            tmp.append(nums[i])
            back(i+1)
            tmp.pop()
                
back(0)