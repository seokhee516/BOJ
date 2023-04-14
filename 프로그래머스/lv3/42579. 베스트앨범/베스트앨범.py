def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i,p)]
        else:
            dic1[g].append((i,p))
        dic2[g] = dic2.get(g, 0) + p
    
    for k, _ in sorted(dic2.items(), key = lambda x:x[1], reverse=True):
        for i, _ in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    
    return answer