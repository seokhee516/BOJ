import sys
input = sys.stdin.readline
n, w, l = map(int, input().split()) # 트럭 개수, 다리 길이, 최대 하중
trucks = list(map(int, input().split())) # 트럭의 무게

bridge = [0] * w # 다리 설정
t = 0 # 다리 건너는 시간

while bridge:
    t += 1
    bridge.pop(0)
    if trucks: # 모든 트럭 확인
        if sum(bridge) + trucks[0] <= l: # 다리에 올라간 무게와 트럭을 합친 무게가 최대하중보다 작을때 
            bridge.append(trucks.pop(0)) # 다리 위에 트럭 올라가기
        else: # 최대하중보다 클 때
            bridge.append(0) # 빈 공간 추가

print(t)

'''
4 2 10
7 4 5 6

[0, 7]
[7, 0]
[0, 4]
[4, 5]
[5, 0]
[0, 6]

8
'''