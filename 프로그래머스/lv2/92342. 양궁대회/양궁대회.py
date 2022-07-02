from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1] # 라이언이 우승할 방법이 없는 경우
    maxgap = -1e9 # 가장 큰 점수 차이 저장
    # 0에서 10까지 길이n의 반복을 허용한 조합 튜플
    # n화살 사용하여 나올 수 있는 모든 점수의 경우
    candidates = list(combinations_with_replacement(range(0, 11), n)) 
    
    # 모든 경우 확인
    for candidate in candidates:
        info2 = [0] * 11 # 라이언 과녁
        apeach, lion = 0, 0 # 어피치 점수, 라이언 점수
        # 라이언 과녁 만들기 
        # 10에서 빼서 리스트에 저장 ex) 10점[0], 0점[10]
        for score in candidate:
            info2[10 - score] += 1
        # enumerate로 0부터 시작 10에서 빼서 점수 계산
        # zip으로 묶어서 (어피치 과녁, 라이언 과녁) 비교
        for score, (a, l) in enumerate(zip(info, info2)):
            # 단 하나의 화살도 맞히지 못한 경우 넘어가기
            if a == l == 0:
                continue
            # 어피치가 많이 맞히거나 동일한 경우 점수 추가
            elif a >= l:
                apeach += (10-score)
            # 라이언이 많이 맞힌 경우 점수 추가
            else:
                lion += (10-score)
        # 라이언 점수가 높은 경우
        if lion > apeach:
            # 점수 차이 구해서
            gap = lion - apeach
            if gap > maxgap:
                maxgap = gap
                answer = info2 # 정답에 라이언 과녁 정보 저장
            
    return answer