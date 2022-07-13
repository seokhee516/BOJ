# 설치or삭제 전에 가능한 구조물인지 확인하는 것이 아니라 일단 설치해놓고 전체를 확인하는 방법
# 따로 메서드를 만들어 가능한지 확인 
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위
            # 나는 보의 한쪽 끝 부분 경우 조건 하나 빠뜨렸다 + 경우 구하지 않아도 in 으로 확인할 수 있다
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False # 아니라면 False
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # 한쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 동시에 보와 연결
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, stuff, operate in build_frame:
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제 해본 뒤
            if not possible(answer): #가능한 구조물인지 확인
                answer.append([x,y, stuff]) # 가능한 구조물 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치 해본 뒤
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과물 반환

'''
내 풀이 - 테스트케이스만 통과
def solution(n, build_frame):
    board = [[-1]*(n+1) for _ in range(n+1)]
    for x,y,a,b in build_frame:
        # 기둥인 경우
        if a == 0:
            # 설치하는 경우
            if b == 1:
                # 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위
                if y == 0 or (x-1>=0 and board[x-1][y]==1) or (board[x][y]==1) or (y-1>=0 and board[x][y-1]==0):
                    board[x][y] = 0
            # 삭제하는 경우
            else:
                if (y+1<=n and board[x][y+1]==0):
                    continue
                else:
                    board[x][y] = -1
        # 보인 경우
        elif a == 1:
            # 설치하는 경우
            if b == 1:
            # 보는 바닥에 설치할 수 없음, 한쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 동시에 보와 연결
                if y > 0:
                    if (y-1>=0 and board[x][y-1]==0) or (x+1<=n and y-1>= 0 and board[x+1][y-1]==0) or (x-1>=0 and board[x-1][y]==1 and x+1<=n and board[x+1][y]==1):
                        board[x][y] = 1
            else:
                if (x-1>=0 and x+1<=n and board[x-1][y]==1 and board[x+1][y]==1):
                    continue
                else:
                    board[x][y] = -1
                    
    result = []
    for i in range(n+1):
        for j in range(n+1):
            if board[i][j] != -1:
                result.append([i,j,board[i][j]])
    result = sorted(result, key = lambda x:(x[0],x[1],x[2]))
    return result
'''