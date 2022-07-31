import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque(sorted(list(map(int, input().split()))))
ans = 0
if n % 2 != 0:
    ans = arr.pop()
while arr:
    ans = max(ans, arr.pop()+arr.popleft())
print(ans)