import sys
input = sys.stdin.readline
from itertools import combinations as cb
# 어려워서 답을 찾아봤당... 백트래킹은 계속 연습해야 할듯...ㅠ

def solution(round):
    global ans
    # round 값이 15 라운드가 되었다면
    if round == 15:
        ans = 1 # 가능한 경기로 바꿔주고
        # 검사 시작
        for sub in res: # 승, 무, 패의 값이 남아있다면
            if sub.count(0) != 3:
                ans = 0 # 불가능한 경기
                break
        return

    t1, t2 = game[round] 
    for x, y in ((0, 2), (1, 1), (2, 0)):
        # 승에 해당하는 원소를 -1 할 때, 패에 해당하는 원소를 -1 해준다.
        # 무에 해당하는 원소를 -1 할 때, 무에 해당하는 다른 원소를 -1 해준다.
        if res[t1][x] > 0 and res[t2][y] > 0:
            res[t1][x] -= 1 
            res[t2][y] -= 1
            solution(round + 1) # round를 순회
            res[t1][x] += 1
            res[t2][y] += 1


answer = []
game = list(cb(range(6), 2)) # 0~5번의 국가가 경기를 할 수 있는 조합을 만들어 저장
# 백트래킹
for _ in range(4):
    data = list(map(int, input().split()))
    res = [data[i:i + 3] for i in range(0, 16, 3)] # res 배열에 3개씩 쪼개어 넣기
    ans = 0
    solution(0) # 총 round를 파라미터로 입력
    answer.append(ans)

print(*answer)