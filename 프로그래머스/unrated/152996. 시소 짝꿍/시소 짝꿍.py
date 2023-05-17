from collections import defaultdict

def solution(weights):
    answer = 0
    info = defaultdict(int)
    # 1:1, 2:3, 1:2, 3:4
    for w in weights:
        answer += info[w] + info[w*2] + info[w/2] + info[(w*2)/3] + info[(w*3)/2] + info[(w*4)/3] + info[(w*3)/4]
        info[w] += 1
        # print(info, w, answer)
    # print(info)
    return answer