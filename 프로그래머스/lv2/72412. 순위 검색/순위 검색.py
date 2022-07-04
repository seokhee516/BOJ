from itertools import combinations
from collections import defaultdict
import bisect
def solution(info, query):
    answer = []
    # info의 정보를 통해 나올 수 있는 모든 경우와 그에 해당하는 코테 점수값은 저장
    # 모든 경우는 아무리 커도 108개이다
    dd = defaultdict(list)
    for i in info:
        infosplit = i.split()
        score = int(infosplit.pop()) # 코테 점수 분리

        dd[''.join(infosplit)].append(score) # javabackendjuniorpizza 이런식으로 넣기
        # '-' 조건 처리해주기 위해 길이 0부터 3까지 가능한 모든 조합 넣기
        for j in range(4):
            candi = list(combinations(infosplit, j)) 
            for c in candi:
                dd[''.join(c)].append(score)
        
    for i in dd:
        dd[i].sort() # bisect를 사용하기 위해 score를 오름차순으로 정렬한다

    for q in query:
        # '-' 은 삭제해주었기 때문에 위와 같이 여러 경우를 모두 만들었다
        querysplit = q.replace('and','').replace('-','').split()
        score = int(querysplit.pop())

        querysplit = ''.join(querysplit)
        # bisect_left는 score가 왼쪽에 들어갈 수 있는 index 값을 뽑아낸다
        # 길이에서 빼면 오름차순으로 score 보다 큰 점수의 개수를 구해준다
        answer.append(len(dd[querysplit])-bisect.bisect_left(dd[querysplit], score))
    return answer
'''
print(dd[i])
{'javabackendjuniorpizza': [150], 
'': [50, 80, 150, 150, 210, 260], 
'java': [80, 150], 
'backend': [50, 80, 150, 260], 
'junior': [80, 150]

print(dd[querysplit],len(dd[querysplit]), querysplit, score, bisect.bisect_left(dd[querysplit], score))
[150] 1 javabackendjuniorpizza 100 0
[150, 210] 2 pythonfrontendseniorchicken 200 1
[260] 1 cppseniorpizza 250 0
[50, 260] 2 backendsenior 150 1
[50, 80, 150, 210] 4 chicken 100 2
[50, 80, 150, 150, 210, 260] 6  150 2
'''