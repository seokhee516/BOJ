import sys
input = sys.stdin.readline
from collections import deque
length = int(input())
arr = [i for i in range(1, length+1)]
arr = deque(zip(arr, map(int, input().split())))

ans = []
while arr:
    num, paper_num = arr.popleft()
    ans.append(num)
    length -= 1
    if length == 0:
        break
    if paper_num > 0:
        paper_num %= length
        arr.rotate(-(paper_num-1))
    else:
        paper_num = -(abs(paper_num)%length)
        arr.rotate(-paper_num)
print(' '.join(map(str, ans)))