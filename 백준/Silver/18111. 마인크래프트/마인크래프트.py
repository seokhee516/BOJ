import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))

height = 0 # 땅의 높이
time = 1e9 # 시간
for f in range(257): # 0층부터 256층 까지 확인 
    remove_h, add_h = 0, 0 # 층마다 블록 초기화
    for i in range(n):
        for j in range(m):
            if ground[i][j] > f: # 층수보다 땅이 높으면
                remove_h += ground[i][j] - f # 제거해야 할 블록 추가
            else: # 층수보다 땅이 낮다면
                add_h += f - ground[i][j] # 더해주어야 할 블록 추가
    invetory = remove_h + b # 인벤토리에 제거하면서 얻은 블록 + 원래 있던 블록 
    if invetory < add_h: # 인벤토리에 있는것보다 더해주어야할 것이 더 많다면
        continue # 채우기 불가 하므로 다음층으로
    tmp = (2 * remove_h) + add_h # 제거작업 2초, 더하는 작업 1초 
    if tmp <= time: # 짧거나 "같은" 시간 (같은 시간 포함해야 높이 높은것 저장됨)
        time = tmp # 새로 저장
        height = f
    
print(time, height)