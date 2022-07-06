import sys
input = sys.stdin.readline
n = int(input())
score = []
for i in range(n):
    score.append(list(map(int, input().split())))
answer = 1e9
start = []
link = []
def backtracking(idx):
    global answer
    # 절반씩 나눠진 경우
    if len(start) == n // 2:
        startscore = 0
        linkscore = 0
        # 스타트님에 없는 값 넣기
        for num in range(n):
            if num not in start:
                link.append(num)
        # 능력치 두개씩 확인
        for i in range(n//2-1):
            for j in range(i+1, n//2):
                startscore += (score[start[i]][start[j]]+score[start[j]][start[i]])
                linkscore +=(score[link[i]][link[j]]+score[link[j]][link[i]])
    
        # 가장 차이가 작은 값 확인
        dif = abs(startscore-linkscore)
        if dif < answer:
            answer = dif
        link.clear()
        return

    for num in range(n):
        # 스타트팀에 수가 존재할때 마지막 숫자가 num 보다 클때
        if start and start[len(start)-1] > num:
            continue # 넘어감
        # num 이 스타트팀에 없을 때
        if num not in start:
            start.append(num)
            backtracking(idx + 1) # 재귀 수행
            start.pop()

backtracking(0)
print(answer)