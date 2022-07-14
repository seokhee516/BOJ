# 처음 구현할 땐 visited를 지정 안해줘서 메모리 초과
# num과 target 값의 범위가 지정되어 있으므로 그 안에서만 확인하면 됨
# dslr 메서드를 효율화함 (list rotate -> 수학적 계산으로 바꿈)
import sys
from collections import deque
input = sys.stdin.readline

def rotate(l, n):
    return l[n:] + l[:n]
def dslr(num, operate):
    if operate == 'D':
        num = (num*2)%10000
    elif operate == 'S':
        num = (num-1)%10000
    elif operate == 'L':
        num = (10*num+(num//1000))%10000
    elif operate == 'R':
        num = ((num%10)*1000+num//10)%10000
    return num

d = ["D","S","L","R"]
def bfs(num, target):
    q = deque([(num, "")])
    while q:
        now, operate = q.popleft()
        visited[now] = True # 방문 표시
        if now == target: # 타겟값과 같으면
            return operate # 명령어 리턴
        for i in range(4): # DSLR, 차례대로 확인
            next = dslr(now, d[i])
            if not visited[next]: # 숫자 방문한 적 없을 때
                q.append((next, operate + d[i])) # 명령어 더해주고
                visited[next] = True # 방문 표시
t = int(input())
for _ in range(t):
    num, target = map(int, input().split())
    visited = [False] * 10000 # num과 target은 0이상 10,000 미만이므로
    print(bfs(num, target))