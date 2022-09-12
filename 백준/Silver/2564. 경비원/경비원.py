# 동근이와 상점의 상대거리가 아니라 (0,0)부터 동근이와 상점의 절대거리 구하기
import sys
input = sys.stdin.readline
w, h = map(int, input().split())
n = int(input())

loc = []
# (0,0)에서 시계방향 이동한 거리 구하기 
for i in range(n+1): # 동근이까지 +1
    d, l = map(int, input().split()) # 방향, 위치
    if d == 1:
        loc.append(l)
    elif d == 2:
        loc.append(w + h + w - l)
    elif d == 3:
        loc.append(w + h + w + h - l)
    elif d == 4:
        loc.append(w + l)

ans = 0
for i in range(n):
    in_course = abs(loc[-1] - loc[i]) # 시계방향
    out_course = 2 * (w + h) - in_course # 반시계방향
    ans += min(in_course, out_course) # 최단 거리 합
print(ans)