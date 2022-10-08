import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
tmp = []
def back(start):
    if len(tmp) == m:
        print(*tmp)
        return
    check = 0 
    for i in range(start, n):
        if not visited[i] and check != nums[i]: 
            tmp.append(nums[i])
            check = nums[i]
            visited[i] = True
            back(i+1)
            visited[i] = False
            tmp.pop()
                
back(0)

'''
4 2
9 7 9 1

1 7
1 9
7 9
9 9
'''