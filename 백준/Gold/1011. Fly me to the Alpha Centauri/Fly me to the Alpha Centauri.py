import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    distance = y-x # 이동할 거리
    cnt = 0 # 이동 횟수
    move = 1 # cnt별 이동 가능 거리
    move_sum = 0 # 이동한 거리의 합
    while move_sum < distance:
        cnt += 1
        move_sum += move # cnt 수에 해당하는 move를 더함
        if cnt % 2 == 0:
            move += 1
    print(cnt)
'''
0 25
이동 횟수 cnt :  1 이동 가능한 거리의 합:  1 (1) cnt로 이동 가능한 거리:  1
이동 횟수 cnt :  2 이동 가능한 거리의 합:  2 (1 1) cnt로 이동 가능한 거리:  1
이동 횟수 cnt :  3 이동 가능한 거리의 합:  4 (1 2 1) cnt로 이동 가능한 거리:  2
이동 횟수 cnt :  4 이동 가능한 거리의 합:  6 (1 2 2 1) cnt로 이동 가능한 거리:  2
이동 횟수 cnt :  5 이동 가능한 거리의 합:  9 (1 2 3 2 1) cnt로 이동 가능한 거리:  3
이동 횟수 cnt :  6 이동 가능한 거리의 합:  12 (1 2 3 3 2 1)cnt로 이동 가능한 거리:  3
이동 횟수 cnt :  7 이동 가능한 거리의 합:  16 (1 2  3 4 3 2 1) cnt로 이동 가능한 거리:  4
이동 횟수 cnt :  8 이동 가능한 거리의 합:  20 (1 2 3 4 4 3 2 1) cnt로 이동 가능한 거리:  4
이동 횟수 cnt :  9 이동 가능한 거리의 합:  25 (1 2 3 4 5 4 3 2 1) cnt로 이동 가능한 거리:  5
'''