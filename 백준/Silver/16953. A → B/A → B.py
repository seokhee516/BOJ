import sys
from collections import deque
input = sys.stdin.readline

num, target = map(int, input().split())
ans = -1
# bfs 이용
q = deque([(num,1)]) # (처음 주어진 값, 최솟값에 1을 더한 값)
while q:
    now, cnt = q.popleft() # 바꾼 숫자, 필요한 연산의 수
    if now == target:
        ans = cnt
        break
    # 2를 곱했을때 target보다 작거나 같으면 q에 넣는다.
    if now * 2 <= target:
        q.append((now*2, cnt+1)) 
    # 1을 수의 가장 오른쪽에 추가했을 때 target보다 작거나 같으면 q에 넣는다.
    if int(str(now)+'1') <= target:
        q.append((int(str(now)+'1'), cnt+1))
print(ans)