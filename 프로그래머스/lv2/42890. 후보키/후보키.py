from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    candidate_keys = []
    for i in range(1, col+1):
        for combi in list(combinations(range(col), i)): # 모든 인적사항 가능한 모든 조합
            # 조합대로 relation 리스트를 만듦
            tmp = [tuple(r[c] for c in combi) for r in relation]
            # 유일성 확인
            if len(set(tmp)) == row: # 중복을 없앤 길이가 원래 relation 로우와 같은지 확인
                put = True
                # 유일성 만족 됐다면 최소성 활인
                for ck in candidate_keys:
                    # ck가 combi의 부분 집합인지 확인 
                    # combi는 적은 조합부터 시작되므로, 최소의 것으로 중복이 안되면서 가능한지 확인
                    if set(ck).issubset(set(combi)):
                        put = False
                        break
                if put:
                    candidate_keys.append(combi)
    answer = len(candidate_keys)
    return answer