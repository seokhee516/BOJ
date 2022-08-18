from itertools import permutations
def solution(k, dungeons):
    n = len(dungeons)
    answer = 0
    tmp = []
    # print(list(permutations(range(n),n)))
    for lst in list(permutations(range(n),n)):
        cnt = 0
        h = k
        for i in lst:
            if h >= dungeons[i][0] and (h-dungeons[i][1]) >= 0:
                # print(lst, i, dungeons[i][0], h-dungeons[i][1])
                cnt += 1
                h-=dungeons[i][1]
                # print(h)
            else:
                break
        tmp.append(cnt)
        if cnt == n:
            break
    answer = max(tmp)
    return answer