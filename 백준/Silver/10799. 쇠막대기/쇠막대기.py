import sys
input = sys.stdin.readline
data = list(input().strip())
up_rod, down_rod, raser, answer = 0, 0, 0, 0

while data:
    if data.pop() == ')':
        if raser == 0:
            raser += 1
        else:
            up_rod += 1
    else:
        if raser == 1:
            # 아래 통나무 자르기
            answer += (down_rod * 1)
            # 위 통나무 자르기
            answer += (up_rod * 2)
            # 위 통나무는 아래 통나무가 됨
            down_rod += up_rod
            up_rod = 0
            # 레이저 사용 끝
            raser = 0
        else:
            # 사용할 레이저 없으면 아래 통나무 정리
            down_rod -= 1
print(answer)