def solution(n, build_frame):
    answer = []
    for x, y, stuff, op in build_frame:
        if op == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제 해본 뒤
            if not possible(answer):
                answer.append([x, y, stuff]) # 가능한 구조물 아니라면 다시 설치
        elif op == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치 해본 뒤
            if not possible(answer):
                answer.remove([x, y, stuff]) # 가능한 구조물 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과 반환 

# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
             # 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # 한쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 동시에 보와 연결
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True
